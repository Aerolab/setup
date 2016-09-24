#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2

name = ''
email = ''
options = { 'developer': '', 'android': '', 'ios': '', 'designer': '', 'web' : '',
            'sublime': '', 'vim': '', 'zsh': '',
            'animations': '', 'showhiddenfiles': '', 'autoupdate': '', }


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "**************************************************************"
  print "Install the XCode Command Line Tools and run this script again"
  print "**************************************************************"
  exit()


# Sudo: Spectacle, ZSH, OSX Settingsql
print "\n\n\nWelcome... TO THE WORLD OF TOMORROW\n\n"

# Basic Info
while name == '':
  name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your email?\n").strip()


# Setup Options
while options['developer'] not in ['y', 'n']:
  options['developer'] = raw_input("Do you want to install Developer Tools? (%s)  " % '|'.join(['y','n']))

if options['developer'] == 'y':
  while options['android'] not in ['y', 'n']:
    options['android'] = raw_input("Do you want to install Android Tools? (%s)  " % '|'.join(['y','n']))

  while options['ios'] not in ['y', 'n']:
    options['ios'] = raw_input("Do you want to install iOS Tools? (%s)  " % '|'.join(['y','n']))

  while options['web'] not in ['y', 'n']:
    options['web'] = raw_input("Do you want to install Web Developer Tools? (%s)  " % '|'.join(['y','n']))

while options['designer'] not in ['y', 'n']:
  options['designer'] = raw_input("Do you want to install Designer Tools? (%s)  " % '|'.join(['y','n']))


# Other Options
while options['sublime'] not in ['y', 'n']:
  options['sublime'] = raw_input("Do you want to install Sublime Text 3 with Plugins? (%s)  " % '|'.join(['y','n']))

while options['vim'] not in ['y', 'n']:
  options['vim'] = raw_input("Do you want to install VIM with Awesome VIM? (%s)  " % '|'.join(['y','n']))

while options['zsh'] not in ['y', 'n']:
  options['zsh'] = raw_input("Do you want to install Oh My Zsh? (%s)  " % '|'.join(['y','n']))

while options['animations'] not in ['y', 'n']:
  options['animations'] = raw_input("Do you want to accelerate OSX animations? (%s)  " % '|'.join(['y','n']))

while options['showhiddenfiles'] not in ['y', 'n']:
  options['showhiddenfiles'] = raw_input("Do you want to show hidden files? (%s)  " % '|'.join(['y','n']))

while options['autoupdate'] not in ['y', 'n']:
  options['autoupdate'] = raw_input("Do you want to update your computer automatically? (Recommended) (%s)  " % '|'.join(['y','n']))


print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print "Creating your Private Key"
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)


# Set computer name (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name.replace(' ', '-')) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)


# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('touch ~/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew tap homebrew/versions')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')


# Install Languages
print "Installing Git+NodeJS+Python+Ruby"
os.system('brew install git node python python3 ruby')
os.system('brew link --overwrite git node python python3 ruby')
os.system('brew install git-flow')

print "Installing Useful Stuff"
os.system('brew install graphicsmagick curl wget sqlite libpng libxml2 openssl')

print "Installing Command Line Tools"
os.system('npm install -g yo bower gulp-cli grunt-cli node-gyp')
os.system('curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash')

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlmarkdown quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch betterzipql font-hack')


print "Installing Fonts"
os.system('brew cask install font-dosis font-droid-sans font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-arial-black font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-georgia font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-lg-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-verdana font-times-new-roman font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-fontawesome font-source-code-pro font-anka-coder')

print "Installing Essential Apps"
os.system('brew cask install iterm2 spectacle the-unarchiver')
os.system('brew cask install google-chrome firefox sourcetree sublime-text atom dropbox skype spotify slack vlc macdown')

os.system('osascript -e \'display notification "We need your password" with title "Mac Setup"\' > /dev/null')
os.system('brew cask install google-hangouts qlimagesize')


# Appropriate Software
if options['developer'] == 'y':
  print "Installing Developer Tools"
  os.system('brew cask install docker kitematic ngrok sequel-pro cyberduck')

if options['android'] == 'y':
  print "Installing Android Tools"
  os.system('brew cask install java')
  os.system('brew cask install android-studio')
  os.system('brew install android-platform-tools')

if options['ios'] == 'y':
  print "Installing iOS Tools"
  os.system('sudo gem install cocoapods')

if options['web'] == 'y':
  print "Installing Web Developer Tools"
  os.system('brew cask install imageoptim imagealpha')
  
if options['designer'] == 'y':
  print "Installing Designer Tools"
  os.system('brew cask install invisionsync iconjar skala-preview lingo')
  #os.system('brew cask install sketch-tool principle framer-studio origami')


# Sublime Text 3 Package Control & Binding
sublime_settings_path = os.path.expanduser("~") + '/Library/Application Support/Sublime Text 3/'
sublime_user_path = sublime_settings_path + 'Packages/User/'

if not os.path.isfile( sublime_settings_path + 'Installed Packages/Package Control.sublime-package'):
  print "Installing Package Control"
  os.system('wget -P ~/Library/Application\ Support/Sublime\ Text\ 3/Installed\ Packages https://packagecontrol.io/Package%20Control.sublime-package')

os.system('ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime')


# Sublime Text 3 with Recommended Packages
if options['sublime'] == 'y':
  print "Customizing Sublime Text"

  if not os.path.exists(os.path.dirname(sublime_settings_path)):
    os.makedirs(os.path.dirname(sublime_settings_path))

  if not os.path.exists(os.path.dirname(sublime_user_path)):
    os.makedirs(os.path.dirname(sublime_user_path))


  # Set the default packages
  if not os.path.isfile( sublime_user_path + 'Package Control.sublime-settings'):
    with open( sublime_user_path + 'Package Control.sublime-settings', 'w+') as f:
      print "Installing Default Packages"

      best_packages = {
        "installed_packages": [
          "BracketHighlighter",
          "Color Highlighter",
          "ColorPicker",

          "Emmet",
          "JavaScript Completions",
          "JavaScriptNext - ES6 Syntax",

          "MarkdownEditing",
          "Material Theme",
          "Sass",
          "SassBeautify",

          "Package Control",
          "SideBarEnhancements",
          "SublimeCodeIntel",
          "FileDiffs",
          "Git",
          "GitGutter",

          "SublimeLinter",
          "SublimeLinter-annotations",
          "SublimeLinter-contrib-sass-lint",
          "SublimeLinter-html-tidy",
          "SublimeLinter-jshint",
          "SublimeLinter-pep8",

          "Web Inspector"
        ]
      }

      prefs_plain = f.read()
      prefs = {}

      if prefs_plain != '':
        prefs = json.loads(prefs_plain)

      for key, value in best_packages.iteritems():
        if key not in prefs:
          prefs[key] = value

      f.write(json.dumps(prefs, sort_keys=True, indent=4, separators=(',', ': ')))


  # Set some default settings
  if not os.path.isfile( sublime_user_path + 'Preferences.sublime-settings'):
    with open( sublime_user_path + 'Preferences.sublime-settings', 'w+') as f:

      print "Configuring Default Settings"

      best_prefs = {
        "always_show_minimap_viewport": False,
        "bold_folder_labels": True,
        #"theme": "Material-Theme.sublime-theme",
        #"color_scheme": "Packages/Material Theme/schemes/Material-Theme.tmTheme",
        "font_options": [
          "gray_antialias",
          "subpixel_antialias"
        ],
        "font_size": 16,
        "indent_guide_options": [
          "draw_normal",
          "draw_active"
        ],
        "line_padding_bottom": 1,
        "line_padding_top": 1,
        "overlay_scroll_bars": "enabled",
        "tab_size": 2,
        "translate_tabs_to_spaces": True,
        "trim_trailing_white_space_on_save": True,
      }

      prefs_plain = f.read()
      prefs = {}

      if prefs_plain != '':
        prefs = json.loads(prefs_plain)

      for key, value in best_prefs.iteritems():
        if key not in prefs:
          prefs[key] = value

      f.write(json.dumps(prefs, sort_keys=True, indent=4, separators=(',', ': ')))


if options['vim'] == 'y':
  print "Installing VIM + Awesome VIM"

  os.system('brew install vim --override-system-vi')
  os.system('git clone https://github.com/amix/vimrc.git ~/.vim_runtime')
  os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')


# Oh-My-ZSH. Dracula Theme for iTerm2 needs to be installed manually
if options['zsh'] == 'y':
  print "Installing Oh-My-Zsh with Dracula Theme"
  os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
  os.system('brew install zsh-syntax-highlighting zsh-autosuggestions')
  os.system('pip install pygments')

  if not os.path.isfile(os.path.expanduser("~") + '/.zshrc'):
    os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc &> /dev/null')

    # Agnoster Theme
    os.system('sed -i -e \'s/robbyrussell/agnoster/g\' ~/.zshrc &> /dev/null')
    # Plugins
    os.system('sed -i -e \'s/plugins=(git)/plugins=(git git-flow brew sublime python node bower npm gem pip pod docker zsh-autosuggestions zsh-syntax-highlighting colorize colored-man-pages copydir copyfile extract)/g\' ~/.zshrc &> /dev/null')

    # Customizations
    os.system('echo "source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc')
    os.system('echo "source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc')
    os.system('echo "alias dog=\'colorize\'" >> ~/.zshrc')

  os.system('chsh -s /bin/zsh &> /dev/null')

  os.system('git clone https://github.com/dracula/iterm.git ~/Desktop/dracula-theme/')


# Random OSX Settings
print "Tweaking OSX Settings"

if options['showhiddenfiles'] == 'y':
  # Finder: show hidden files by default
  os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
  # Finder: show all filename extensions
  os.system('defaults write NSGlobalDomain AppleShowAllExtensions -bool true')


# Finder: allow text selection in Quick Look
os.system('defaults write com.apple.finder QLEnableTextSelection -bool true')
# Check for software updates daily
os.system('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')
# Disable auto-correct
#os.system('defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false')
# Require password immediately after sleep or screen saver begins
os.system('defaults write com.apple.screensaver askForPassword -int 1')
os.system('defaults write com.apple.screensaver askForPasswordDelay -int 0')
# Show the ~/Library folder
os.system('chflags nohidden ~/Library')
# Don’t automatically rearrange Spaces based on most recent use
os.system('defaults write com.apple.dock mru-spaces -bool false')
# Prevent Time Machine from prompting to use new hard drives as backup volume
os.system('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')
# Mute startup sound
os.system('osascript -e \'display notification "Almost There! We need your password again" with title "Mac Setup"\' > /dev/null')
os.system('sudo nvram SystemAudioVolume=%80')


if options['animations'] == 'y':
  print "Tweaking System Animations"
  os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.1')
  os.system('defaults write com.apple.dock expose-animation-duration -float 0.15')
  os.system('defaults write com.apple.dock autohide-time-modifier -float 0.2')
  os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.5')


if options['autoupdate'] == 'y':
  print "Enabling Automatic Brew Updates & Upgrades"
  os.system('brew tap domt4/autoupdate')
  os.system('brew autoupdate --start --upgrade')


# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Open Spectacle (Needs to be enabled manually)
os.system('open -a "Spectacle"')


# Clean Up
os.system('brew cleanup && brew cask cleanup')


print ""
print ""
print "*************************************"
print "Enabling FileVault"
os.system('sudo fdesetup enable')
print ""

print "*************************************"
print "Your SSH Public Key Is:"
with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
  print f.read()
print ""

if options['zsh'] == 'y':
  print "*************************************"
  print "Remember to set up iTerm2:"
  print "* Go to iTerm2 > Preferences > Profiles > Colors Tab"
  print "  * Load Presets..."
  print "  * Import..."
  print "  * Pick Desktop > dracula-theme > iterm > Dracula.itermcolors"
  print "* Go to iTerm2 > Preferences > Profiles > Text Tab"
  print "  * Regular Font"
  print "  * 12pt Menlo for Powerline Font"
  print ""

if options['sublime'] == 'y':

  print "*************************************"
  print "Please launch Sublime Text to finish setup"
  print "Material Theme needs to be enabled manually"
  print "On User Preferences, add: \"theme\": \"Material-Theme.sublime-theme\""
  print ""

print "*************************************"
print "Remember to restart your Mac"
print "*************************************"


