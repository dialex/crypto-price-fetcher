from invoke import task


@task()
def clean(ctx):
    """Deletes generated files"""
    ctx.run("rm -rf test/output")
    ctx.run("rm -f prices.txt")


@task(clean)
def app(ctx):
    """Runs the script"""
    ctx.run("python main.py")


@task(clean)
def test(ctx):
    """Runs unit tests"""
    ctx.run("python -m unittest discover -b")


@task()
def install(ctx):
    """Installs tools required to run and develop the app"""
    ctx.run("pipenv install")


# TODO: implement the tasks below

# desc "Fetches the prices of your favorite crypto currencies"
# task :fetch => [:fetch_prices] do end

# desc "Cleans generated files"
# task :clean => [:clean_install, :clean_run] do end

# desc "Tells you how you can use this app"
# task :help do
#   sh('rake -T', verbose: false)
# end

# def execute(ctx):
#     #run clean
#     #run fetch
