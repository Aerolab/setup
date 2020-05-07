#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2
import subprocess

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


# Sudo: Spectacle, ZSH, OSX Settings
print "\n\nWelcome... TO THE WORLD OF TOMORROW\n"

# Basic Info
while name == '':
  name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your email?\n").strip()


# Setup Options
while options['designer'] not in ['y', 'n']:
  options['designer'] = raw_input("Do you want to install Designer Tools? (%s)  " % '|'.join(['y','n']))

while options['developer'] not in ['y', 'n']:
  options['developer'] = raw_input("Do you want to install Developer Tools? (%s)  " % '|'.join(['y','n']))

if options['developer'] == 'y':
  while options['web'] not in ['y', 'n']:
    options['web'] = raw_input("Do you want to install Web Developer Tools? (%s)  " % '|'.join(['y','n']))

  while options['android'] not in ['y', 'n']:
    options['android'] = raw_input("Do you want to install Android Tools? (%s)  " % '|'.join(['y','n']))

  while options['ios'] not in ['y', 'n']:
    options['ios'] = raw_input("Do you want to install iOS Tools? (%s)  " % '|'.join(['y','n']))


# Other Options
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


def show_notification(text):
  os.system('osascript -e \'display notification "'+ text +'" with title "Mac Setup"\' > /dev/null')


print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub') :
  print "Creating your Private Key"
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)


# Set computer name & git info (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name.replace(' ', '-')) # Doesn't support spaces
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)
os.system('git config --global user.name "%s"' % name)
os.system('git config --global user.email "%s"' % email)

# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('touch ~/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap homebrew/cask-versions')
os.system('brew tap homebrew/cask-fonts')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')


# Install Languages
print "Installing Git+NodeJS+Python+Ruby"
os.system('brew install git node python python3 ruby')
os.system('brew link --overwrite git node python python3 ruby')
os.system('brew unlink python && brew link --overwrite python') # Fixes an issue with pip
os.system('brew install git-flow git-lfs')
os.system('git lfs install')

print "Installing Useful Stuff"
os.system('brew install graphicsmagick curl wget sqlite libpng libxml2 openssl')
os.system('brew install bat tldr tree')

print "Installing Command Line Tools"
os.system('npm install -g yo gulp-cli node-gyp serve ndb')

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlstephen qlmarkdown quicklook-csv quicklook-json webpquicklook suspicious-package quicklookase qlvideo qlimagesize epubquicklook qlprettypatch qlvideo')

print "Installing Fonts"
os.system('brew cask install font-dosis font-droid-sans-mono-for-powerline font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-source-code-pro font-hack')
# font-anka-coder isn't working

print "Installing Essential Apps"
os.system('brew cask install iterm2 spectacle the-unarchiver')
os.system('brew cask install google-chrome firefox sourcetree sublime-text visual-studio-code atom dropbox skype spotify slack vlc typora')

os.system('brew cask fetch google-hangouts qlimagesize')
show_notification("We need your password")
os.system('brew cask install google-hangouts qlimagesize')


# Appropriate Software
if options['developer'] == 'y':
  print "Installing Developer Tools"
  os.system('brew cask install docker ngrok sequel-pro cyberduck tunnelblick insomnia')
  os.system('curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash')
            
if options['android'] == 'y':
  print "Installing Android Tools"
  os.system('brew cask fetch java')
  show_notification("We need your password")
  os.system('brew cask install java')
  os.system('brew cask install android-studio')
  os.system('brew install android-platform-tools')

if options['ios'] == 'y':
  print "Installing iOS Tools"
  show_notification("We need your password")
  os.system('sudo gem install cocoapods')
  show_notification("We need your password")
  os.system('sudo gem install fastlane --verbose')

if options['web'] == 'y':
  print "Installing Web Developer Tools"
  os.system('brew cask install imageoptim imagealpha xnconvert')
  
if options['designer'] == 'y':
  print "Installing Designer Tools"
  os.system('brew cask install invisionsync skala-preview')
  os.system('brew cask install adapter handbrake')
  os.system('brew cask install origami-studio')

if options['vim'] == 'y':
  print "Installing VIM + Awesome VIM"

  os.system('brew install vim --with-override-system-vi')
  os.system('git clone https://github.com/amix/vimrc.git ~/.vim_runtime')
  os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')

# Oh-My-ZSH. Dracula Theme for iTerm2 needs to be installed manually
if options['zsh'] == 'y':
  print "Installing Oh-My-Zsh with Dracula Theme"
  show_notification("We need your password")

  # Setup Adapted from https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh
  if os.system('test -n "$ZSH"') != 0:
     os.system('export ZSH=~/.oh-my-zsh')

  if os.system('test -n "$ZSH_CUSTOM"') != 0:
     os.system('export ZSH_CUSTOM=~/.oh-my-zsh/custom')

  if os.system('test -d "$ZSH"') != 0:
    os.system('umask g-w,o-w && git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git $ZSH')

  if os.system('test -f ~/.zshrc') != 0:
    os.system('cp $ZSH/templates/zshrc.zsh-template ~/.zshrc')

  os.system('git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions')
  os.system('git clone git://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting')

  # If the user has the default .zshrc tune it a bit
  if (subprocess.call(['bash', '-c', 'diff <(tail -n +6 ~/.zshrc) <(tail -n +6  ~/.oh-my-zsh/templates/zshrc.zsh-template) > /dev/null']) == 0):

    # Agnoster Theme
    os.system('sed -i -e \'s/robbyrussell/agnoster/g\' ~/.zshrc &> /dev/null')
    # Plugins
    os.system('sed -i -e \'s/plugins=(git)/plugins=(git brew sublime node npm docker zsh-autosuggestions zsh-syntax-highlighting colored-man-pages copydir copyfile extract)/g\' ~/.zshrc &> /dev/null')

    # Customizations
    os.system('echo "alias dog=\'bat\'" >> ~/.zshrc')
    # Don't show the user in the prompt
    os.system('echo "DEFAULT_USER=\`whoami\`" >> ~/.zshrc')
            
    os.system('echo "export NVM_DIR=\"\$HOME/.nvm\"\n[ -s \"\$NVM_DIR/nvm.sh\" ] && . \"\$NVM_DIR/nvm.sh\" # This loads nvm" >> ~/.zshrc')

  # Remove the 'last login' message
  os.system('touch ~/.hushlogin')

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


if options['animations'] == 'y':
  print "Tweaking System Animations"
  os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.1')
  os.system('defaults write com.apple.dock expose-animation-duration -float 0.15')
  os.system('defaults write com.apple.dock autohide-delay -float 0')
  os.system('defaults write com.apple.dock autohide-time-modifier -float 0.3')
  os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.5')
  os.system('killall Dock')


if options['autoupdate'] == 'y':
  print "Enabling Automatic Brew Updates & Upgrades"
  os.system('brew tap domt4/autoupdate')
  os.system('brew autoupdate --start --upgrade')


# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Open Spectacle (Needs to be enabled manually)
os.system('open -a "Spectacle"')

# Open Dropbox
os.system('open -a "Dropbox"')


# Clean Up
os.system('brew cleanup && brew cask cleanup')


# Mute startup sound
show_notification("We need your password")
os.system('sudo nvram SystemAudioVolume=%00')


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

show_notification("All done! Enjoy your new macOS!")

  
# Change the shell if necessary
if options['zsh'] == 'y':
  os.system('chsh -s /bin/zsh &> /dev/null')
