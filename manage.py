import os
from webapp import create_app
from webapp.config import DevConfig
from flask_script import Manager, Server



#default to dev config
#env = os.environ.get("WEBAPP_ENV", "dev")
app = create_app('webapp.config.DevConfig')



manager = Manager(app)
manager.add_command("server", Server(host='0.0.0.0', port='5000'))



@manager.shell
def make_shell_context():
    return dict(
        app=app,
        User = User,
        Role=Role
    )

if __name__ == "__main__":
    manager.run()
