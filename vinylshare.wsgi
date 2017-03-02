import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/vynilshare/venv/lib/python2.7/site-packages')

INTERP = os.path.expanduser("~/venv/bin/python")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/venv/bin')
sys.path.insert(0,'$HOME/venv/lib/python2.7/site-packages/django')
sys.path.insert(0,'$HOME/venv/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/vynilshare/vinylshare')

os.environ['DJANGO_SETTINGS_MODULE'] = 'vinylshare.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/vynilshare/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()