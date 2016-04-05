#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2

print "Welcome... TO THE WORLD OF TOMORROW"

all_roles = ['developer', 'designer', 'other']

name = ''
email = ''
role = ''

while name == '':
  name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your email at Aerolab?\n").strip()

while role not in all_roles:
  role = raw_input("What do you do at Aerolab? (%s)\n" % '|'.join(all_roles))


print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


if os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print "You already have a Private Key"
else:
  print "Creating your Private Key"
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)


print "Installing XCode Tools"
# XCode Essentials from https://github.com/donnemartin/dev-setup
os.system('git clone https://github.com/donnemartin/dev-setup.git')
os.system('./dev-setup/.dots bootstrap osxprep')
os.system('rm -rf ./dev-setup')

print "Installing Brew & Brew Cask"
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

print "Installing JS+Python+Ruby"
os.system('brew install git node python python3 ruby go')
os.system('brew link --overwrite git node python python3 ruby')

print "Installing Useful Stuff"
os.system('brew install graphicsmagick curl wget sqlite libpng libxml2 openssl letsencrypt')

print "Installing Package Managers"
os.system('npm install -g yo bower gulp grunt grunt-cli node-gyp')
os.system('npm install -g pageres pageres-cli')

print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlmarkdown qlimagesize quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch betterzipql font-hack')

print "Installing Fonts"
os.system('brew cask install font-dosis font-droid-sans font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-arial font-arial-black font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-georgia font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-lg-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-verdana font-times-new-roman font-ubuntu font-pt-mono font-pt-sans font-pt-serif')

print "Installing Essential Apps"
os.system('brew cask install iterm2 spectacle the-unarchiver')
os.system('brew cask install google-chrome firefox sourcetree sublime-text3 atom dropbox skype spotify slack google-hangouts vlc macdown')

if role in ['developer']:
  print "Installing Developer Tools"
  os.system('brew cask install dockertoolbox')
  #os.system('brew install android-platform-tools')
  #os.system('brew cask install android-studio')

if role in ['designer']:
  print "Installing Designer Tools"
  os.system('brew cask install invisionsync iconjar skala-preview')
  #os.system('brew cask install sketch-tool principle framer-studio origami')


if not os.path.isfile(os.path.expanduser("~") + '/Library/Application Support/Sublime Text 3/Installed Packages/Package Control.sublime-package'):
  print "Adding Package Control to Sublime Text"
  os.system('wget -P ~/Library/Application\ Support/Sublime\ Text\ 3/Installed\ Packages https://packagecontrol.io/Package%20Control.sublime-package')


print "Installing Oh-My-Zsh with Dracula Theme"
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc &> /dev/null')
os.system('chsh -s /bin/zsh &> /dev/null')
os.system('sed -i -e \'s/robbyrussell/agnoster/g\' ~/.zshrc &> /dev/null')

os.system('git clone https://github.com/zenorocha/dracula-theme/ ~/Desktop/dracula-theme/')


print "Tweaking Finder Settings"

if role in ['developer']:
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
os.system('sudo nvram SystemAudioVolume=", "')


if role in ['developer']:
  print "Tweaking System Animations"
  os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.1')
  os.system('defaults write com.apple.dock expose-animation-duration -float 0.15')
  os.system('defaults write com.apple.dock autohide-time-modifier -float 0.2')
  os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.5')

# Set computer name (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)

# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')


print ""
print ""
print "*************************************"
print "Enabling FileVault"
os.system('sudo fdesetup enable')

print ""
print ""
print "*************************************"
print "Your Public Key Is:"

with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
  print f.read()

print ""
print ""
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
print "*************************************"
print "Remember to restart your Mac"
print "*************************************"


