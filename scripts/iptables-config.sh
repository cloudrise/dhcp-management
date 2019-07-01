iptables -A INPUT -p tcp -s YOUR_IP --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 22 -j DROP


iptables -A INPUT -p tcp -s YOUR_IP --dport 3306 -j ACCEPT
iptables -A INPUT -p tcp -s 0.0.0.0/0 --dport 3306 -j DROP