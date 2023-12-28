# 0x09-web_infrastructure_design

In this project, I have built a web stack as part of the sysadmin/devops track.
The web stack diagram covers the components I have implemented, and I can
provide detailed explanations for each component's function. Additionally, I
have implemented system redundancy to ensure high availability and fault
tolerance. As part of this project, I have gained knowledge of key acronyms such
as LAMP (Linux, Apache, MySQL, PHP), SPOF (Single Point of Failure), and QPS
(Queries Per Second). I am proficient in explaining the significance of each
acronym within the context of the web stack.

## What I learned
- **Network Basics**: Fundamental concepts and principles of computer networking.
- **Server**: An overview of server functionality and its role in network communication.
- **Web Server**: Explanation of web server's function in serving web content to clients.
- **DNS**: Introduction to the Domain Name System and its role in translating domain names to IP addresses.
- **Load Balancer**: Overview of load balancers and their role in distributing network or application traffic.
- **Monitoring**: Introduction to system monitoring and its importance in tracking system performance and health.
- **Database**: An explanation of databases and their role in storing and managing structured data.
- **Web Server vs. App Server**: Differentiating the roles and functions of web servers and application servers.
- **DNS Record Types**: Overview of different types of DNS records and their purposes.
- **Single Point of Failure**: Understanding the concept of a single point of failure in a system or network.
- **Avoiding Downtime**: Strategies for minimizing downtime during code deployment or updates.
- **High Availability Cluster**: Explanation of high availability clusters, including active-active and active-passive configurations.
- **HTTPS**: Introduction to HTTPS (Hypertext Transfer Protocol Secure) and its role in secure communication over a computer network.
- **Firewall**: An overview of firewalls and their role in network security.

## Application server vs web server
The terms "application server vs. web server" are commonly used together on the Internet, despite their contrasting implications. Web servers primarily handle requests for static content from a website, while application servers provide access to business logic for generating dynamic content. In a typical setup, web servers deliver static content, and application servers generate dynamic content. A reverse proxy and load balancer are used to route traffic to the appropriate server. The distinction between the two types of servers has become less clear due to their overlapping functionalities. NGINX Plus is a widely used solution for efficiently managing web and application servers, providing features such as reverse proxy, load balancing, caching, and request routing.
