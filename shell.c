#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<sys/stat.h>
#include<fcntl.h>
typedef struct node
{
	char name[400];
	int cond;
	int procid;
}node;
char *in,*out;
node backproc[100]; 
int cnt=0;
pid_t ppid;
char HOME[200];
int len;
#define DELIMS " \t\r\n" 
void sig_handle(int sign)
{
	if (sign==2 ||sign==3)
	{
		fflush(stdout);
		printf("\n");
		char *path=malloc(100);
		getcwd(path,100);
		if(path==NULL)
			perror("cwd: ");
		char *point;
		char pa[100];
		point=strstr(path,HOME);
		if(point)
		{
			path=path+len;
			strcpy(pa,path);
			strcpy(path,"~");
			strcat(path,pa);
		}
		char buf[100];
		gethostname(buf,100);
		char *user=malloc(100);
		user=getlogin();
		printf("%s@%s:%s> ",user,buf,path);
		fflush(stdout);
		signal(SIGQUIT,sig_handle);
		signal(SIGINT,sig_handle);
	}
	if(sign==20)
	{
		kill(ppid,SIGTSTP);
		signal(SIGTSTP,sig_handle);
	}
	return;
}
void child_sig(int signo)
{
	int pid;
	int temp;
	pid=waitpid(WAIT_ANY, &temp, WNOHANG);
	int i;
	for(i=0;i<cnt;i++)
	{
		if(backproc[i].procid==pid && backproc[i].cond==1)
		{
			backproc[i].cond=0;
			printf("\n%s %d exited normally\n",backproc[i].name,backproc[i].procid);
			//prompt();

			char *path=malloc(100);
			getcwd(path,100);
			if(path==NULL)
				perror("cwd: ");
			char *point;
			char pa[100];
			point=strstr(path,HOME);
			if(point)
			{
				path=path+len;
				strcpy(pa,path);
				strcpy(path,"~");
				strcat(path,pa);
			}
			char buf[100];
			gethostname(buf,100);
			char *user=malloc(100);
			user=getlogin();
			printf("%s@%s:%s> ",user,buf,path);
			fflush(stdout);
		}
	}
	signal(SIGCHLD, child_sig);
	return;
}
int main()
{
	getcwd(HOME,200);
	if(HOME==NULL)
		perror("cwd ");
	len=strlen(HOME);
	signal(SIGINT,SIG_IGN);
	signal(SIGINT,sig_handle);
	signal(SIGCHLD,SIG_IGN);
	signal(SIGCHLD,child_sig);
	signal(SIGTSTP,SIG_IGN);
	signal(SIGTSTP,sig_handle);
	signal(SIGQUIT,SIG_IGN);
	signal(SIGQUIT,sig_handle);
	while(1)
	{
		int flag=0;
		char *p,*pa;
		char *name=malloc(1000);
		char *n=malloc(1000);
		char **farr=malloc(sizeof(char *)*1);
		int j;
		for(j=0;j<1;j++)
			farr[j]=malloc(sizeof(char **)*100);
		char *path=malloc(100);
		getcwd(path,100);
		if(path==NULL)
			perror("cwd: ");
		char *point;
		char paa[100];
		point=strstr(path,HOME);
		if(point)
		{
			path=path+len;
			strcpy(paa,path);
			strcpy(path,"~");
			strcat(path,paa);
		}
		char buf[100];
		gethostname(buf,100);
		char *user=malloc(100);
		user=getlogin();
		printf("%s@%s:%s> ",user,buf,path);
		int c;
		if((c=getchar())==EOF)
		{
			printf("\n");
			continue;
		}
		else
			ungetc(c,stdin);
		scanf ("%[^\n]s", name);
		strcpy(n,name);
		getchar();
		char *token,*brr[10000];
		token=strtok(name,";");
		int rr=0;
		while(token!=NULL)
		{
			brr[rr]=token;
			rr++;
			token=strtok(NULL,";");
		}
		int ii;
		for(ii=0;ii<rr;ii++)
		{
			int index=0;
			char *pch;
			pch=strtok(brr[ii],DELIMS);
			while(pch!=NULL)
			{
				if (strcmp(pch,">")==0 || strcmp(pch,"<")==0 || strcmp(pch,"|")==0)
				{
					if(strcmp(pch,">")==0) 
					{
						if(flag==2)
							flag=3;
						else flag=1;
						out=strtok(NULL,DELIMS);
						if(out==NULL)
						{
							printf("Incorrect Syntax\n");
							break;
						}
					}
					if(strcmp(pch,"<")==0) 
					{
						if (flag == 1)
							flag=3;
						else flag=2;
						in=strtok(NULL,DELIMS);
						if(in==NULL)
						{
							printf("Incorrect syntax\n");
							break;
						}
					}
					if(strcmp(pch,"|")==0) //PIPES
					  {
					  flag=5;	
					  int infile, outfile, oldpipe[2],newpipe[2];
					  int stdin_c=dup(STDIN_FILENO), stdout_c=dup(STDOUT_FILENO);
					  int flag=0;
					  char *pipec[100];
					  char **command=malloc(sizeof(char *)*1);
					  command[0]=malloc(sizeof(char **)*1000);
					  char *t;
					  int i=0;
					  //PARSING- TO SEPARATE PIPE COMMANDS
					  t=strtok(n,"|");
					  while(t!=NULL)
					  {
						  //printf("t---%s\n ",t);
						  pipec[i++]=t;
						  pipec[i-1][strlen(pipec[i-1])]='\0';
						  t=strtok(NULL,"|");
					  }
					  pipec[i]=NULL;
					  //PARSING TO SPLIT INTO COMMANDS
					  int j=0;
					  for(j=0;j<i;j++)
					  {
						  char *t1,*t2,*co;
						  char *command[100];
						  char *inp;
						  int in=0;
						  char pi[1000];
						  strcpy(pi,pipec[j]);
						  t1=strtok(pipec[j],"<");
						  char t11[1000];
						  strcpy(t11,t1);
						  if(strcmp(t1,pi)!=0)
						  {
							  flag=2;
							  inp=strtok(NULL,DELIMS);
							  
						  }
						  char pip[1000];
						  strcpy(pip,pi);
						  char t22[1000];
						  t2=strtok(pi,">");
						  strcpy(t22,t2);
						  if(strcmp(t2,pip)!=0)
						  {
							  flag=1;
							  out=strtok(NULL,DELIMS);
							  
						  }
						  if(flag==2)
						  {
							  
							  co=strtok(t11,DELIMS);
							  while(co!=NULL)
							  {
								  command[in++]=co;
								  co=strtok(NULL,DELIMS);
							  }
							  command[in]=NULL;
							  infile=open(inp,O_RDONLY,777);
							  if(infile<0)
								  perror("File not created\n");
							  else
							  {
								  dup2(infile,0);
							  }
						  }
						  else if(flag==1)
						  {
							  co=strtok(t22,DELIMS);
							  while(co!=NULL)

							  {
								  command[in++]=co;
								  co=strtok(NULL,DELIMS);
							  }
							  command[in]=NULL;
							  outfile=open(out,O_RDWR|O_CREAT,777);
							  if(outfile<0)
								  perror("File not created\n");
							  else
								  dup2(outfile,1);
						  }
						  else
						  {
							  co=strtok(pipec[j],DELIMS);
							  while(co!=NULL)
							  {
								  command[in++]=co;
								  co=strtok(NULL,DELIMS);
							  }
							  command[in]=NULL;
						  }
						  //PIPE IMPLEMENTATION
						  if(j<i-1)
							  pipe(newpipe);
						  pid_t pid=fork();
						  if(j>0 && j<=i-1)
						  {
							  dup2(oldpipe[0],0);
							  close(oldpipe[0]);
							  close(oldpipe[1]);
						  }
						  if (pid==0)
						  {
							  if(j<i-1)
							  {
								  dup2(newpipe[1],1);
								  close(newpipe[1]);
								  close(newpipe[0]);
							  }
							  int r=execvp(command[0],command);
							  if(r<0)
							  {
								  perror("connamd not found");
								  exit(1);
							  }
						  }
						  else
						  {
							  int r;
							  waitpid(pid,&r,0);
							  if(j<i-1)
							  {
								  oldpipe[0]=newpipe[0];
								  oldpipe[1]=newpipe[1];
							  }
						  }
					  }
					  close(oldpipe[0]);
					  close(newpipe[0]);
					  close(oldpipe[1]);
					  close(newpipe[1]);
					  dup2(stdin_c, 0);
					  dup2(stdout_c, 1);
					  close(stdin_c);
					  close(stdout_c);
					  break;
					  }
				}
				else if(strcmp(pch,"&")==0)
				{
					flag=4;
				}
				else
					farr[index++]=pch;
				pch=strtok(NULL,DELIMS);
			}
			farr[index]=pch;
			if(flag==5)
				continue;
			if(farr[0]==NULL)
				continue;
			else if(strcmp(brr[0],"quit")==0)
				exit(0);
			else if(strcmp(farr[0],"cd")==0)
			{
				int r;
				if(index==1)
				{ r=chdir(HOME);
					if(r<0)
						perror("error in changing directory\n");
				}
				else if(strcmp(farr[1],"~")==0 || strcmp(farr[1],"~/")==0)
				{
					r=chdir(HOME);
					if(r<0)
						perror("chdir ");
				}
				else
				{
					r=chdir(farr[1]);
					if(r<0)
						perror("chdir ");
				}
			}
			else if(strcmp(farr[0],"jobs")==0)
			{
				int i=0;int j=0;
				for(i=0;i<cnt;i++)
				{
					if(backproc[i].cond==1)
					{
						j++;
						printf("[%d] %s [%d]\n",j,backproc[i].name,backproc[i].procid);
					}
				}
			}
			else if(strcmp(farr[0],"kjob")==0)
			{
				int pno=atoi(farr[1]);
				int i,j=0;
				for(i=0;i<cnt;i++)
				{
					if(backproc[i].cond==1)
						j++;
					if(j==pno)
						break;
				}
				if(i==cnt)
					printf("No such job exists\n");
				else
					if(kill(backproc[i].procid,atoi(farr[2]))<0)
						perror("kill ");
			}
			else if(strcmp(farr[0],"overkill")==0)
			{
				if(farr[1]!=NULL)
					printf("overkill takes no argument\n");
				else
				{
					int i;
					for(i=0;i<cnt;i++)
					{
						if(backproc[i].cond==1)
							kill(backproc[i].procid,9);
					}
					cnt=0;
					printf("All processes killed\n");
				}
			}
			else if(strcmp(farr[0],"fg")==0)
			{
				if(farr[1]==NULL || farr[2]!=NULL)
					printf("invalid command\n");
				else
				{
					int pno=atoi(farr[1]);
					int s;
					int i,j=0;
					for(i=0;i<cnt;i++)
					{
						if(backproc[i].cond==1)
							j++;
						if(j==pno)
							break;
					}
					if(i==cnt)
						printf("No such process exists\n");
					else
					{
						if(waitpid(backproc[i].procid,&s,0)<0)
							perror("wait ");
						backproc[i].cond=0;
					}
				}
			}
			else
			{
				int status;
				pid_t pid;
				pid=fork();
				if (pid<0)
				{
					perror("Fork");
					exit(-1);
				}
				else if(pid==0)
				{

					if(flag==3)
					{
						int fi,fo;
						fi=open(in,O_RDONLY);
						dup2(fi,0);
						fo=open(out,O_RDWR|O_CREAT,S_IRWXU);

						dup2(fo,1);
					}

					if(flag==2)
					{
						int fi;
						fi=open(in,O_RDONLY);

						dup2(fi,0);
						close(fi);
					}

					if (flag==1)
					{

						int fo;
						fo=open(out,O_RDWR|O_CREAT,S_IRWXU);

						dup2(fo,1);
						close(fo);
					}

					int r=execvp(farr[0],farr);
					if(r<0)
						perror("Execvp ");
				}
				else
				{

					if (flag==4)
					{
						backproc[cnt].procid=pid;
						backproc[cnt].cond=1;
						int i,j=0;
						for(i=1;farr[i]!=NULL;i++)
						{
							strcat(farr[j]," ");
							strcat(farr[j],farr[i]);
						}
						strcpy(backproc[cnt].name,farr[0]);
						cnt++;
					}
					else
					{
						ppid=pid;
						if(waitpid(pid, &status, WUNTRACED)<0)
							perror("Wait ");
						if(WIFSTOPPED(status))
						{
							backproc[cnt].procid=pid;
							backproc[cnt].cond=1;
							int i,j=0;
							for(i=1;farr[i]!=NULL;i++)
							{
								strcat(farr[j]," ");
								strcat(farr[j],farr[i]);
							}
							strcpy(backproc[cnt].name,farr[0]);
							cnt;
						}
					}
				}
			}

		}
	}
	return 0;
}
