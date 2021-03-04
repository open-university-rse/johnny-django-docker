from django.contrib.auth.models import User

def run():

    paul = User.objects.create_superuser(
        username="paul", email="paul@johnny.org", password="password"
    )
    tun = User.objects.create_superuser(
        username="tun", email="tun@johnny.org", password="password"
    )
    irum = User.objects.create_superuser(
        username="irum", email="irum@johnny.org", password="password"
    )

    # researcher_group = Group.objects.get(name='Researchers')
    # researcher_group.user_set.add(paul)
    # researcher_group.user_set.add(jef)
