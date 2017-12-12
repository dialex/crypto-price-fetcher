require_relative 'logging.rb'
require_relative 'helpers.rb'

task :default => [:run]

desc "Do it!"
task :run => [:run_impl] do end

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

task :run_impl do
  log_step 'Doing stuff...'
  price = extract_price(get_data('bitcoin'))
  log 'done, price is ' + price.to_s
end
