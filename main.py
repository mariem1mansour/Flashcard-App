from website import create_app
app=create_app()
if __name__=='__main__':
  app.run(debug=True)  #every time we change in somrthing in the code ,it 's going automatically rerun the web server 
