from invoke import task


@task()
def clean(ctx):
    """Deletes generated files"""
    ctx.run("rm -rf test/output")
    ctx.run("rm -f prices.txt")


@task(clean)
def app(ctx):
    """Fetches the prices of your favorite crypto currencies"""
    ctx.run("python app.py")


@task(clean)
def test(ctx):
    """Runs unit tests"""
    ctx.run("python -m unittest discover -b")


@task()
def install(ctx):
    """Installs tools required to run and develop the app"""
    ctx.run("pipenv install")


@task()
def help(ctx):
    """Lists all available commands and usage"""
    ctx.run("invoke --list")
