# ==================== Imports ====================

require_relative 'logging.rb'
require_relative 'helpers.rb'

# ==================== Constants ====================

config_filepath = 'config.txt'
output_filepath = 'prices.txt'

# ==================== Tasks ====================

task :default => [:clean, :install, :run]

desc "Do it!"
task :run => [:fetch_prices] do end

desc "Cleans generated files"
task :clean => [:clean_install, :clean_run] do end

desc "Installs dependencies required to run the app"
task :install => [:install_user] do end

desc "Installs tools required to develop the app"
task :dev => [:install_dev] do end

# ==================== Implementation ====================

task :clean_install do
  log_step 'Cleaning previous installation...'
  sh('gem cleanup')
end

task :clean_run do
  log_step 'Cleaning previous execution...'
  sh("rm -rf #{output_filepath}")
end

task :install_user do
  log_step 'Installing dependencies...'
  sh('bundle install')
  ok 'Installed'
end

task :install_dev do
  warn 'You need to run the \'dev-tools.sh\' script.'
end

task :fetch_prices do
  log_step 'Fetching prices...'

  if !File.file?(config_filepath) then
    err "Could not locate the file `#{config_filepath}`."
    warn 'Create the configuration file and write one coin ticker symbol per line. To list the supported coin tickers do `rake list`.'
    exit
  end

  File.readlines(config_filepath).each do |line|
    price = extract_price(get_data(line.strip))

    f = File.open(output_filepath, 'a')
    f.puts(price)
    f.close
  end

  ok 'Prices available at ' + output_filepath
end
