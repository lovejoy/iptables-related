#改变数据包流向，做端口或者数据镜像相关的内容
--oif 出口interface
--iif 
--gw 指定网关来路由数据
--continue 路由这个包并且继续穿越后续的规则
--tee (未知）
 iptables -A POSTROUTING -t mangle -p icmp -j ROUTE -oif eth1 强制所有的流出icmp包通过eth1
 iptables -A POSTROUTING -t mangle -p tcp --dport 80 -j ROUTE --oif tunl1 --continue 强制流出的http包通过tunl1并继续后面的规则
 iptables -A POSTROUTING -t mangle -p tcp --dport 22 -j ROUTE --gw w.x.y.z --continue 转发所有的ssh包到网关w.x.y.z，同时穿越规则
 iptables -A PREROUTING -t mangle -p icmp -i eth0 -j ROUTE -iif eth1 改变进入网络界面eth0所有的icmp包到eth1上
 iptables -A PREROUTING -t mangle -p tcp --dport 7 -j ROUTE --gw w.x.y.z  
 iptables -A POSTROUTING -t mangle -sport 7 -j ROUTE --gw w.x.y.z 复制（镜像）特定源和目的地址的流量到本地的一个ECHO 服务器。
