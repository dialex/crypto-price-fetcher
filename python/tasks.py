from invoke import task


@task()
def run(ctx):
    """Runs the script"""
    ctx.run("python main.py")


def install(ctx):
    """Installs tools required to run and develop the app"""
    ctx.run("pipenv install")


# TODO: implement the tasks below

# desc "Fetches the prices of your favorite crypto currencies"
# task :fetch => [:fetch_prices] do end

# desc "Cleans generated files"
# task :clean => [:clean_install, :clean_run] do end

# desc "Installs dependencies required to run the app"
# task :install => [:install_user] do end

# desc "Installs tools required to develop the app"
# task :dev => [:install_dev] do end

# desc "Tells you how you can use this app"
# task :help do
#   sh('rake -T', verbose: false)
# end
