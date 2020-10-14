#
#
# To send an OpenFlow Message telling a switch to send packets out a port, do 
# the following, replacing <PORT> with the port number the switch should send 
# the packets out:
#
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can 
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet 
    #      (for example, s1 would have switch_id ==1, s2 would have switch_id ==2, etc...)
    find_ICMP = packet.find('icmp')
    find_IP = packet.find('ipv4')

    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.idle_timeout = 30
    msg.hard_timeout = 30

    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    msg.data = packet_in
    self.connection.send(msg)

    if find_IP is None:
       msg.data = packet_in
       msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
       self.connection.send(msg)
       return
    
    if find_ICMP:
      if find_ICMP.srcip == "123.45.67.89":
         self.connection.send(msg)

    if find_IP:
      if find_IP.srcip == "123.45.67.89" and find_ICMP:
          msg.data = packet_in 
          self.connection.send(msg)
          return
      elif find_IP.srcip == "123.45.67.89" and find_IP.dstip == "10.5.5.50":
          msg.data = packet_in
          self.connection.send(msg)
          return
      else:
          if switch_id == 1:
             if port_on_switch == 8:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 13))
                self.connection.send(msg)
                return
             if port_on_switch == 13:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 8))
                self.connection.send(msg)
                return
          if switch_id == 2:
             if port_on_switch == 9:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 15))         
                self.connection.send(msg)
                return
             if port_on_switch == 15:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 9))
                self.connection.send(msg)
                return
          if switch_id == 3:
             if port_on_switch == 10:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 17))           
                self.connection.send(msg)
                return
             if port_on_switch == 17:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 10))
                self.connection.send(msg)
                return
          if switch_id == 5:
             if port_on_switch == 12:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 20))           
                self.connection.send(msg)
                return
             if port_on_switch == 20:
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port = 12))
                self.connection.send(msg)
                return
          if switch_id == 4:
             if find_IP.dstip == "10.1.1.10":   
                if port_on_switch == 16:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 14))
                   self.connection.send(msg)
                   return
                if port_on_switch == 18:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 14))
                   self.connection.send(msg)
                   return
                if port_on_switch == 19:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 14))
                   self.connection.send(msg)
                   return
                if port_on_switch == 12:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 14))
                   self.connection.send(msg)
                   return
             if find_IP.dstip == "10.2.2.20":
                if port_on_switch == 14:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 16))
                   self.connection.send(msg)
                   return
                if port_on_switch == 18:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 16))
                   self.connection.send(msg)
                   return
                if port_on_switch == 19:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 16))
                   self.connection.send(msg)
                   return
                if port_on_switch == 11:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 16))
                   self.connection.send(msg)
                   return
             if find_IP.dstip == "10.3.3.30":
                if port_on_switch == 14:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 18))
                   self.connection.send(msg)
                   return
                if port_on_switch == 16:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 18))
                   self.connection.send(msg)
                   return
                if port_on_switch == 11:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 18))
                   self.connection.send(msg)
                   return
                if port_on_switch == 19:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 18))
                   self.connection.send(msg)
                   return
             if find_IP.dstip == "123.45.67.89":
                if port_on_switch == 14:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 19))
                   self.connection.send(msg)
                   return
                if port_on_switch == 16:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 19))
                   self.connection.send(msg)
                   return
                if port_on_switch == 18:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 19))
                   self.connection.send(msg)
                   return
                if port_on_switch == 19:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 19))
                   self.connection.send(msg)
                   return
             if find_IP.dstip == "10.5.5.50":
                if port_on_switch == 14:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 11))
                   self.connection.send(msg)
                   return
                if port_on_switch == 16:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 11))
                   self.connection.send(msg)
                   return
                if port_on_switch == 11:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 11))
                   self.connection.send(msg)
                   return
                if port_on_switch == 18:
                   msg.data = packet_in
                   msg.actions.append(of.ofp_action_output(port = 11))
                   self.connection.send(msg)
                   return
  
  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # THis is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
