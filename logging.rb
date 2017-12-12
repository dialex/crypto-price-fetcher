def log (msg)
  puts "#{msg}"
end

def log_step (msg)
  puts ""
  puts ">>> #{msg}".blue
end

def warn (msg)
  puts "[!] WARNING: #{msg}".yellow
end

def err (msg)
  puts "[X] ERROR: #{msg}".red
end

def ok (msg)
  puts "✔ #{msg}".green
end

# extends String to have colour codes
class String
  def colorize(color_code)
    "\e[#{color_code}m#{self}\e[0m"
  end

  def red
    colorize(31)
  end

  def green
    colorize(32)
  end

  def yellow
    colorize(33)
  end

  def blue
    colorize(36)
  end
end
