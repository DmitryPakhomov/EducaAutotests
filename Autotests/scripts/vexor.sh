#!/usr/bin/env bash

set -e

# Places where we'll get a Mozilla Firefox browser and Selenium's webdriver for it
FIREFOX_BROWSER_DOWNLOAD_URL=https://download-installer.cdn.mozilla.net/pub/firefox/releases/57.0.2/linux-x86_64/ru/firefox-57.0.2.tar.bz2
FIREFOX_WEBDRIVER_DOWNLOAD_URL=https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz


# Places where we'll get a Google Chrome browser and Selenium's webdriver for it
# CHROME_BROWSER_DOWNLOAD_URL=https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
CHROME_BROWSER_DOWNLOAD_URL=https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/522736/chrome-linux.zip
CHROME_WEBDRIVER_DOWNLOAD_URL=https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip


#
FIREFOX_BINARY=./bin/firefox/firefox
FIREFOX_WD_BINARY=./bin/geckodriver

CHROME_BINARY=./bin/chrome/google-chrome
CHROME_WD_BINARY=./bin/chromedriver


# Install Firefox (if need)
command -v "${FIREFOX_BINARY}" >/dev/null 2>&1 || {
  name="./artefacts/${FIREFOX_BROWSER_DOWNLOAD_URL##*/}"

  if [ ! -e "${name}" ]; then
    echo "A local copy of firefox not found, trying to fetch"
    curl -L -o "${name}" "${FIREFOX_BROWSER_DOWNLOAD_URL}"
  else
    echo "Found a local copy in ${name}"
  fi

  tar -xjf "${name}" -C ./bin
}

# Install Firefox webdriver (if need)
command -v "${FIREFOX_WD_BINARY}" >/dev/null 2>&1 || {
  name="./artefacts/${FIREFOX_WEBDRIVER_DOWNLOAD_URL##*/}"

  if [ ! -e "${name}" ]; then
    echo "A local copy of firefox webdriver not found, trying to fetch"
    curl -L -o "${name}" "${FIREFOX_WEBDRIVER_DOWNLOAD_URL}"
  else
    echo "Found a local copy in ${name}"
  fi

  tar -zxf "${name}" -C  ./bin
  chmod +x "${FIREFOX_WD_BINARY}"
}

# Install Chrome (if need)
command -v "${CHROME_BINARY}" >/dev/null 2>&1 || {
  name="./artefacts/${CHROME_BROWSER_DOWNLOAD_URL##*/}"
  if [ ! -e "${name}" ]; then
    echo "A local copy of chrome not found, trying to fetch"
    curl -L -o "${name}" "${CHROME_BROWSER_DOWNLOAD_URL}"
  else
    echo "Found a local copy in ${name}"
  fi

  # These lines actual for the debian package, so still keep it.
  # dpkg -x "${name}" ./chrome
  # mv ./chrome/opt/google/chrome ./bin
  # rm -rf ./chrome

  unzip -o "${name}" -d ./bin
  mv ./bin/chrome-linux ./bin/chrome

}

# Install Chrome webdriver (if need)
command -v "${CHROME_WD_BINARY}" >/dev/null 2>&1 || {
  name="./artefacts/${CHROME_WEBDRIVER_DOWNLOAD_URL##*/}"

  if [ ! -e "${name}" ]; then
    echo "A local copy of CHROME webdriver not found, trying to fetch"
    curl -L -o "${name}" "${CHROME_WEBDRIVER_DOWNLOAD_URL}"
  else
    echo "Found a local copy in ${name}"
  fi

  unzip  -o "${name}" -d ./bin
  chmod +x "${CHROME_WD_BINARY}"
}
