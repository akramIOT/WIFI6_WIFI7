
## This Module is used to analyze some Performance Modelling of  MPTCP with WIFI7  Technology  with MiniNet
# Ref:  https://mininet-wifi.github.io/   ###
# @Author: Akram Sheriff 
# Date:  13th of  April 2021
#!/usr/bin/python
"""MPTCP Demo"""

from mininet.log import setLogLevel, info
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mn_wifi.net import Mininet_wifi
from select import poll

def topology():
     """
             *AP2--h4          * s7
           *(MLO)           *     *    *
     STA1*               * s6       *-- s9--h10
          *            *     *     *. . .
           * (MLO)   *        *   *   . . .
            * AP3--h5          s8 ......
     """

     net = Mininet_wifi()
     info("*** Creating nodes\n")
     sta1 = net.addStation('sta1', wlans=2, ip='10.0.0.10/8', min_x=10, max_x=130,min_y=10, max_y=130, min_v=20, max_v=50)
     ap2 = net.addAccessPoint('ap2', mac='00:00:00:00:00:02', equipmentModel='TLWR740N',protocols='OpenFlow10', ssid= 'Test_WIFI7_ap2', mode= 'g',channel= '6', position='55,17,0' )
     ap3 = net.addAccessPoint('ap3', mac='00:00:00:00:00:03', equipmentModel='TLWR740N',protocols='OpenFlow10', ssid= 'Test_WIFI7_ap3', mode= 'n',channel= '1', position='50,11,0' )
     h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.254/8' )
     h5 = net.addHost( 'h5', mac='00:00:00:00:00:05', ip='192.168.0.254/24' )
     s6 = net.addSwitch( 's6', mac='00:00:00:00:00:06', protocols='OpenFlow10' )
     s7 = net.addSwitch( 's7', mac='00:00:00:00:00:07', protocols='OpenFlow10' )
     s8 = net.addSwitch( 's8', mac='00:00:00:00:00:08', protocols='OpenFlow10' )
     s9 = net.addSwitch( 's9', mac='00:00:00:00:00:09', protocols='OpenFlow10' )
     h10 = net.addHost( 'h10', mac='00:00:00:00:00:10', ip='192.168.1.254/24' )
     c11 = net.addController( 'c11', controller=RemoteController, ip='127.0.0.1' )
     info("*** Configuring wifi nodes\n")
     net.configureWifiNodes()
     info("*** Associating and Creating links\n")
     net.addLink(ap2, sta1, 0, 0)
     net.addLink(ap3, sta1, 0, 1)

