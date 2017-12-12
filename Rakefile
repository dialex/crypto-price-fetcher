require_relative 'logging.rb'
require_relative 'helpers.rb'

task :default => [:run]

desc "Do it!"
task :run => [:fetch_prices] do end

desc "Installs dependencies required to run the app"
task :install => [:install_user] do end

desc "Installs tools required to develop the app"
task :dev => [:install_dev] do end

# ==================== Implementation ====================

task :install_user do
  bundle install
end

task :install_dev do
  sh('./bigbang.sh')
end

task :fetch_prices do
  config_filepath = 'config.txt'
  output_filepath = 'prices.txt'

  log_step 'Fetching prices...'
  File.readlines(config_filepath).each do |line|
    price = extract_price(get_data(line.strip))

    f = File.open(output_filepath, 'a')
    f.puts(price)
    f.close
  end

  ok 'Prices available at ' + output_filepath
end
