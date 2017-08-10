from flask import Flask
from flask import request, render_template
import json
import psycopg2

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #print(request.endpoint)
    title = "JB's Title"
    folders = ['ABOUT','SKILLS','PROJECTS']
    folder_dict = {'ABOUT':['tomato','darkred'],'SKILLS':['khaki','darkkhaki'],'PROJECTS':['cadetblue','slateblue']}
    colors=['white','blue']
    return render_template("base.html",title=title,folders=folders,folder_dict=folder_dict)

@app.route('/testroute', methods=['GET'])
def testroute():
    #BUTTON_NAME : [selected background color, hover background color, alternative choice]
    return_data = {'ABOUT':['tomato','tomato','darkred'],'SKILLS':['khaki','khaki','darkkhaki'],'PROJECTS':['cadetblue','cadetblue','slateblue'], 'project_sub_folder':['podast-project.html']}
    return json.dumps(return_data)

@app.route('/aws_route')
def aws_route(db,user,passw,host):
    conn = psycopg2.connect(database=db,user=user, password=passw, host=host, port='5432', sslmode='prefer')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test;")
    x = cur.fetchone()
    return render_template("aws.html",info=x)

#if __name__ == '__main__':
#    app.run()

# @app.route('/resume')
# def resume():
#     title="Resume"
#     folders = ['ABOUT','SKILLS','PROJECTS']
#     return render_template('resume.html',title=title,folders=folders)
#
# @app.route('/about')
# def about():
#     title="About"
#     folders = ['ABOUT','SKILLS','PROJECTS']
#     return render_template("about.html", title=title, folders=folders)
#
# @app.route('/projects')
# def about():
#     title="projects"
#     folders = ['ABOUT','SKILLS','PROJECTS']
#     return render_template("projects.html", title=title, folders=folders)
# some junk_-_- piUDHJcc+53JGfbweUtb+bvVjCmPFtd/M4o4qt5s
# AKIAI4XMZFBDWI43N5UA
