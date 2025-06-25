# writeup.md

## 1. Resource Analysis

| Criteria         | Virtual Machine (VM)                                                                        | App Service (Web App)                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Cost**         | Higher and less predictable, including OS licensing and manual scaling. Charged for uptime. | Cost-effective for web apps. Flexible pricing; pay-as-you-go. Scaling and patching included. |
| **Scalability**  | Manual scaling and load balancing needed; must configure yourself.                          | Automatic scaling—vertical/horizontal—handled by Azure.                                      |
| **Availability** | You set up redundancy and backup. Must manage patching and recovery.                        | High availability built-in. Microsoft manages redundancy, failover, and health monitoring.   |
| **Workflow**     | Full control, but you maintain OS, security updates, and deployment.                        | Streamlined workflow: CI/CD with GitHub Actions; no server/OS maintenance needed.            |

---

## 2. Solution Choice & Justification

For this project, I deployed the Article CMS using **Azure App Service** (not a VM).

**Justification:**

* Azure App Service is designed for hosting modern web applications and provides easy integration with Azure SQL Database and Blob Storage.
* It supports CI/CD using GitHub Actions, so I can push updates to GitHub and trigger automated deployments.
* No manual server setup or OS management was needed—everything is handled as a Platform-as-a-Service.
* App Service made it much easier to add Microsoft Authentication, set up environment variables, and manage the deployment pipeline.

---

## 3. How the App Would Change if the Decision Was Different

If I had chosen a **VM**:

* I would have to manually install and configure Python, Flask, ODBC drivers, Nginx/Apache, and set up all security, networking, and backup jobs myself.
* Scaling would be manual (adding/removing VMs, setting up load balancers).
* The deployment process would be more complex and time-consuming (requiring scripts for provisioning, patching, and updating).
* Managing secrets and environment variables would require extra setup for security.

If requirements changed (e.g., custom OS-level software or complex scheduled jobs), I might switch to a VM, but for a standard CMS web app, **App Service is the best fit**.

---

## 4. Summary Table

| Requirement        | App Service           | VM             |
| ------------------ | --------------------- | -------------- |
| Ease of deployment | Easy (GitHub Actions) | Complex/manual |
| Scaling            | Automatic (one click) | Manual         |
| Maintenance        | Minimal (Azure)       | Full (User)    |
| Cost               | Lower for web apps    | Higher         |
| Control            | Platform-level        | Full OS-level  |

---
Certainly! Here’s a well-written, detailed section for your `writeup.md` to explain **how the app and its requirements would change if you chose a different solution, and what other needs might require changes.**

---

## 5. Application Changes and Additional Needs

If I had chosen to deploy the CMS on a Virtual Machine instead of Azure App Service, the application setup and maintenance would be significantly different. Using a VM would provide full control over the operating system, network configuration, and installed software, making it possible to meet advanced customization or legacy requirements. However, this also means I would need to manage OS updates, security patching, server monitoring, and manual scaling, increasing the complexity and operational overhead.

If my application required custom background services, scheduled tasks outside the web server, or specialized software dependencies not supported by App Service, I would need to switch to a VM and update my deployment and maintenance procedures. This could include writing custom scripts for automated backups, implementing robust monitoring solutions, or configuring advanced networking and security settings (such as VPN integration or firewalls). Additionally, any requirement for high-performance workloads, GPU support, or non-standard runtime environments might also make a VM—or even Azure Kubernetes Service—a better choice.

Choosing App Service means I sacrifice some control over the infrastructure, but I gain simplicity, automated scaling, built-in high availability, and lower maintenance costs. If future requirements demand more control or custom components, the infrastructure and workflows would need to be adapted accordingly.

---
## 6. References

* [Microsoft: App Service vs. Virtual Machines](https://learn.microsoft.com/en-us/azure/app-service/overview)
* [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
* [Best practices for cloud apps](https://learn.microsoft.com/en-us/azure/architecture/best-practices/web-app)
* https://ahex.co/azure-vm-machines-vs-app-services-making-the-right-choice/
* https://azure.microsoft.com/en-gb/products/app-service
---
