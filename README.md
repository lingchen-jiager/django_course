学习django过程，自己敲的代码记录

使用miniconda管理python虚拟环境时，一键启动manage.py的bat脚本

要保证保存成cmd时，文件类型为ansi类型，否则中文会乱码。

```cmd
call C:/ProgramData/miniconda3/Scripts/activate.bat commonuse


d:

cd "D:\OneDrive\应用\remotely-save\obsidian文件库\obsidian远程同步\学习任务\django vue python全栈开发学习\django vue课程学习代码\django_course_code\"

cmd /K  ""./django-env/Scripts/activate.BAT"&&cd creat_app&&python manage.py runserver"



```


或者用以下方式：

```cmd
"C:\ProgramData\miniconda3\Scripts\activate.bat" "C:\ProgramData\miniconda3" && d: &&conda activate commonuse &&cd "D:\OneDrive\应用\remotely-save\obsidian文件库\obsidian远程同步\学习任务\django vue python全栈开发学习\django vue课程学习代码\django_course_code\"&&"django-env/Scripts/activate.BAT"&&cd creat_app&&python manage.py runserver


```

或者

使用\^将不同行分割开来，当然仅仅是视觉上分割，增加可读性。\^为bat文件的续航符，表示本行未完，会将下一行的代码和上一行自动连接。
```cmd
 "C:\ProgramData\miniconda3\Scripts\activate.bat" "C:\ProgramData\miniconda3" ^
 && conda activate commonuse ^
 && d: ^
 && cd /d "D:\OneDrive\应用\remotely-save\obsidian文件库\obsidian远程同步\学习任务\django vue python全栈开发学习\django vue课程学习代码\django_course_code" ^
 && ""django-env\Scripts\activate.BAT"" ^
 && cd creat_app ^
 && python manage.py runserver

```