
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/thexrd/xrdlib/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/xrd.svg)](https://badge.fury.io/py/xrd)
[![CircleCI](https://img.shields.io/circleci/project/github/thexrd/integration_tests/master.svg?label=integration)](https://circleci.com/gh/thexrd/integration_tests)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/e3070763b579456380822b2909259070)](https://www.codacy.com/app/xrd/xrd?utm_source=github.com&utm_medium=referral&utm_content=thexrd/xrd&utm_campaign=Badge_Coverage) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e3070763b579456380822b2909259070)](https://www.codacy.com/app/xrd/xrd?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thexrd/xrd&amp;utm_campaign=Badge_Grade)
[![codebeat badge](https://codebeat.co/badges/5748b416-7398-4d08-8b49-e4285ef9a82d)](https://codebeat.co/projects/github-com-thexrd-xrd-master)


# XRD - BlockChain Ledger 

> Python-based blockchain ledger utilizing hash-based one-time merkle tree signature scheme (XMSS) instead of ECDSA. Proof-of-work block selection via the cryptonight algorithm. Future transition to POS with signed iterative hash chain reveal scheme which is both probabilistic and random.
>
> Hash-based signatures means larger transactions (3kb per tx, binary), longer keypair generation times and the need to record 'state' of transactions as each keypair can only be used once safely. Merkle tree usage enables a single address to be used for signing numerous transactions (up to 2^13 computationally easily enough). Currently XMSS/W-OTS+ are natively supported with extensible support for further cryptographic schemes inbuilt. 

# Documentation


## XRD Node


Running a XRD node strengthens the network, supports the decentralization and further verifies transactions on the network. This is an essential function of the decentralized architecture XRD relies on.This allows you to run a private secure node to communicate with the XRD blockchain.You can use the node to connect the explorer, wallet, and ephemeral messaging features to the gRPC XRD functions.


> There are various options available for connecting to the API and setup options for the node can be configured through a user set configuration file.

#### Requirements


You can run XRD on most operating systems, though Ubuntu 16.04 is recommended.
- Support for AES-NI
- Support for avx2 (Used by keccak library for hashing functions)
- HDD with enough storage for the blockchain as it grows
- Reliable network connection
- Python3.6
- 64 bit processor


Abridged instructions for installing XRD on Ubuntu:

```
# Update and Upgrade packagessudo apt update && sudo apt upgrade -y

# Install Required dependenciessudo apt-get -y install swig3.0 python3-dev python3-pip build-essential pkg-config libssl-dev libffi-dev libhwloc-dev libboost-dev

## Install CMAKE version 3.10.3 manuallycd /opt && sudo wget https://github.com/Kitware/CMake/releases/download/v3.10.3/cmake-3.10.3.tar.gz && sudo tar zxvf cmake-3.10.3.tar.gz && cd cmake-3.10.3/ && sudo ./configure && sudo make -j2 && echo -e '## Adding cmake version 3.10.3\nPATH=$PATH:/opt/cmake-3.10.3/bin' >> ~/.bashrc && source ~/.bashrc

# Make sure setuptools is the latest
pip3 install -U setuptools

# Install XRD
pip3 install -U xrd
```


If things worked correctly you will now find the?start_xrd?package and the?xrd?package. Adding the?--help?flag to each will print the various function details.



#### Getting Started


Installing XRD is simple, and is possible on most modern operating systems. The install relies on?python3.5?or newer and the?pip3?python package install system.


**Update and Dependencies**

You will need to start with a fully updated system. You will also need a few additional packages depending on your setup. See the correct section for your OS and install all of the requirements.


##### Ubuntu


Update your system ensuring you have the latest packages:

```
# Issue the following command to update software
sudo apt update && sudo apt upgrade -y
```


Now install all the required dependencies:

```
# Install the required packages for XRD
sudo apt-get -y install swig3.0 python3-dev python3-pip build-essential pkg-config libssl-dev libffi-dev libhwloc-dev libboost-dev
```


XRD requires?cmake v3.10.3?to be installed. Ubuntu repositories will install an incompatible version. Please install manually as shown below. If you already have?cmake?installed, please uninstall first.

```
# Install the required packages for XRD
cd /opt && sudo wget https://github.com/Kitware/CMake/releases/download/v3.10.3/cmake-3.10.3.tar.gz && sudo tar zxvf cmake-3.10.3.tar.gz && cd cmake-3.10.3/ && sudo ./configure && sudo make -j2 && echo -e '## Adding cmake version 3.10.3\nPATH=$PATH:/opt/cmake-3.10.3/bin' >> ~/.bashrc && source ~/.bashrc
```

##### Redhat/fedora

Update:

```
# Update
dnf update
```

Dependencies:

```
# Install required packages
dnf install swig cmake gcc gcc-c++ redhat-rpm-config python3-devel python-devel hwloc-devel boost-devel
```

You will need to install?cmake v3.10.3?manually.
[Please follow the guide from the cmake documentation](https://cmake.org/install/)

##### MacOS

To build in OSX Please install?brew?if you have not already.

```
# Install brew with
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
```

This will prompt you through a few questions while it installs.Having Issues? Please follow the instructions found at the brew main page:?[https://brew.sh/](https://brew.sh/)

```
# Update brew
brew update
brew install python3 swig boost hwloc
```

You will need to install?cmake v3.10.3?manually.

[Please follow the guide from the cmake documantation](https://cmake.org/install/)

##### Windows 10

Windows support in the current version is limited. An alternative is to install Ubuntu using the Linux Subsystem for Windows.

###### Ubuntu on Linux Subsystem for Windows (WSL)


You can run a full node in Windows utilizing the Windows Subsystem for Linux. There are a ton of guides out there on setting this up. Here are a few links to get you going.The Windows Subsystem for Linux (WSL) is a new Windows 10 feature that enables you to run native Linux command-line tools directly on Windows, alongside your traditional Windows desktop and modern store apps.You can [follow?these](https://msdn.microsoft.com/en-us/commandline/wsl/install-win10) instructions?to install Ubuntu using Linux Subsystem,

###### Links - Installing Ubuntu in Windows 10
[Windows Subsystem for Linux Documentation](https://docs.microsoft.com/en-us/windows/wsl/about)

[Google Is Your Friend (install+ubuntu+in+windows+10)](https://www.google.com/search?hl=en&as_q=install+ubuntu+in+windows+10&as_epq=)

[WSL Blog](https://blogs.msdn.microsoft.com/wsl/)


#### Install XRD

Now that we have a freshly updated system, the installation of XRD is a breeze, XRD uses python3 to install. The install is the same for all operating systems after you have installed the requirements. Using the Python3 package installer?pip3?we will install XRD.

Before we install XRD make sure setupTools is the latest.

```
pip3 install -U setupTools
```

After this completes install XRD with:

```
pip3 install -U xrd
```

This will install the XRD package and any required dependencies.

#### Start XRD Node

Now that we have XRD installed we can?start_xrd?and begin syncing the node. This will begin the node in the foreground of the shell. If you would like to continue using the shell you can either pass the?--quiet?flag or run the command in a?screen?session ( you will need screen installed ).

```
start_xrd
```


This will print out the details of the running XRD processes. For a more verbose output you can pass the?-l?option with?DEBUG, INFO,WARNING,ERROR,CRITICAL?depending on the level of information you need.

```
start_xrd-l DEBUG
```

The node will sync the entire blockchain to your computer, make sure you have enough space. after syncing the chain you will begin seeing blocks added. Congrats, your XRD node is working.

###### Help

If you would like to see all of the options you can pass along the command line simply add?--help?to the end of the command above.

```
start_xrd--help
```

This will print all of the various options available.

```
usage: start_xrd [-h] [--mining_thread_count MINING_THREAD_COUNT] [--quiet]
                 [--xrddir XRD_DIR] [--no-colors]
                 [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                 [--network-type {mainnet,testnet}]
                 [--miningAddress MINING_ADDRESS]
                 [--mockGetMeasurement MEASUREMENT] [--debug] [--mocknet]

XRD node

optional arguments:
  -h, --help            show this help message and exit
  --mining_thread_count MINING_THREAD_COUNT, -m MINING_THREAD_COUNT
                        Number of threads for mining
  --quiet, -q           Avoid writing data to the console
  --xrddir XRD_DIR, -d XRD_DIR
                        Use a different directory for node data/configuration
  --no-colors           Disables color output
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --loglevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
  --network-type {mainnet,testnet}
                        Runs XRD Testnet Node
  --miningAddress MINING_ADDRESS
                        XRD Wallet address on which mining reward has to be
                        credited.
  --mockGetMeasurement MEASUREMENT
                        Warning: Only for integration test, to mock
                        get_measurement
  --debug               Enables fault handler
  --mocknet             Enables default mocknet settings
```

#### Configuration


By default when the node is started it will?**NOT**?mine any coins. You will have to enable using a configuration file in the?~/.xrd/?directory.

The configuration file is where you will change any options you want XRD to observe. You can grab a copy of the file and details about all of the settings in our?Configuration GuideThe defaults can be used to run a XRD node, though you may need to change some of the directives for your use.

#### Mining XRD
> If you want to mine using a XRD node, see the guide for?Mining XRD Solo?or the?pool guide?to get started.

## Mining with a XRD Node


You can setup a XRD mining node on a PC or server. This will allow you to mine XRD while also running a node on the XRD network. You simply need to enable mining on the XRD node in a config file to begin mining XRD.

 **Requirements**
 - XRD installed and fully synced
 - XRD Wallet to send rewards to
 - A little time to set it up
 - Local or remote shell connection (ssh)
 
 
>This write-up assumes that you have a fully functioning XRD node running and fully synced with the blockchain. If you need to, see the guide at?docs.thexrdorg/node/XRDnode


While connected to the computer running xrd you can see the state of the node by entering?xrd state?into the command line. This will print out the blockheight of the local node as well as some other information. Check that this is the same height as the?XRD explorer?shows.Once fully synced you can start mining by editing the config file found in?~/.xrd/config.yml?enabling mining.


#### Configuration


To begin mining you will need to create and edit a file located in the default XRD directory?~/.xrd/config.yml. There are a ton of configurations and settings you can tweak, however for this guide we are only concerned with the mining settings.


> For a complete guide of the configuration settings, please see the?XRD Node Configurations?guide.


Create the config file and add these settings to the file if not already created.

```
nano ~/.xrd/config.yml 
```

```
# ======================================
#    Mining Configuration
# ======================================
# mining_enabled: False# mining_address: ''
# mining_thread_count: 0  
# 0 auto detect thread count based on number of processors
#
```

These are the default settings the node is currently using. Change the values and remove the # to begin mining.

> You need to enter a valid XRD address, change the?False?value to a?True?value, and set the thread count if you want to adjust.


Once you have made your changes the file will look something like this.

> Note the XRD address shown needs to be replaced, unless you want to donate some quanta!

```
# ======================================
#    Mining Configuration# ======================================
 mining_enabled: True
 mining_address: 'XRD1F2c4stA5qtwL2kWFoVxmqwqzYpn8kjP8P'
 mining_thread_count: 0  # 0 to auto detect thread count based on CPU/GPU number of processors
 #
```

#### Restart XRD


Restart the xrd node to begin mining with the new changes.

```
start_xrd 
```


Once the node re-syncs with the network and catches up it will begin mining the current blocks on the chain You will see the rewards in the wallet you have specified in the configuration file.

You can also enter the following to print the state of the node


```
xrd state 
```


* * *
