# Replication package for "On the Use of ChatGPT for Code Review"
This repository includes the replication package and results for MSR Challenge 2024. 
If you want to use this tool in your research, please cite the following papers:
```
To appear after the acceptance
```

## Source code
 Our main source code is located in 'Python/src' directory.

### Require
・Docker(> 24.0.5)

### Run
This program is designed to run on docker. A python program will be executed by Docker compose.<br>
You can run it with the following commands: 
```
docker-compose build
docker-compose up
```
 
### Outputted table 
The program extracts the code review comments using ChatGPT sharing links. They are contained in the "pr_commit_list". 
| Attribute   | Description                                             |
|-------------|---------------------------------------------------------|
| Directory   | Snapshot name                                           |
| Author      | Author who introduced this mention                      |
| create_time | When the author created this pull request               |
| Reviewer    | Who mentioned this shared ChatGPT link                  |
| Body        | Description of this pull request                        |
| Mention     | The context when this shared ChatGPT link was mentioned |
| URL         | URL to the mentioned source                             |

## Annotated results
With the output of the above program, two of the authors performed the manual inspection independently and manually. 
The annotated classification result is stored in the ``results/classification.xlsx'' file. 