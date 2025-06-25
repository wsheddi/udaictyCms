
# writeup.md

## 1. Resource Analysis

| Criteria         | Virtual Machine (VM)                                                                                        | App Service (Web App)                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Cost**         | Higher ongoing costs due to VM size, OS licensing, and manual scaling. You pay for up time, not just usage. | More cost-effective for web apps; flexible pricing tiers; only pay for what you use; scaling is built-in. |
| **Scalability**  | Manual scaling required (need to configure/load-balance VMs yourself).                                      | Automatic scaling available, including vertical and horizontal scaling with just a few clicks.            |
| **Availability** | Requires manual setup of redundancy, backups, and monitoring.                                               | High availability and built-in redundancy; Microsoft manages failover and health for you.                 |
| **Workflow**     | More control, but more maintenance: you must patch, update, and monitor OS/app.                             | Simple deployment workflow; integrates with GitHub Actions and DevOps; no OS maintenance needed.          |

---

## 2. Solution Choice & Justification

For this project, I chose to deploy the Article CMS using **Azure App Service** instead of a Virtual Machine.

* **Reasoning**: App Service is specifically designed for web applications, offering easier deployment, scaling, and monitoring out of the box. It eliminates the need for manual OS patching, backups, and scaling tasks that VMs require.
* **Cost and Simplicity**: It is more cost-effective for a typical web app, supports auto-scaling, and the workflow (CI/CD, rollback, diagnostics) is much simpler and less error-prone compared to managing a VM.

---

## 3. How the App Would Change if the Decision Was Different

* If I needed **greater control** over the OS, network, or had to install custom software dependencies (e.g., for legacy apps), I might choose a VM instead.
* **App Service** works best for Python, Node, .NET, and similar web apps, but a VM is better suited if you require a custom stack or need to support workloads that can’t be run in a Platform-as-a-Service environment.
* If my application required running background services or scheduled tasks outside the typical web server model, using a VM (or combining App Service with Azure Functions/VM) might be necessary.

**Infrastructure Needs If Requirements Change:**

* If high performance or OS-level customization is needed, I would switch to a VM and update my deployment scripts (e.g., add Ansible or Bash scripts).
* If security needs change (such as custom firewalls or VPN), a VM or Virtual Network integration might be required.

---

## 4. Summary Table

| Requirement        | App Service            | VM                        |
| ------------------ | ---------------------- | ------------------------- |
| Ease of deployment | Easy                   | Moderate/Complex          |
| Scaling            | Automatic/Configurable | Manual                    |
| Maintenance        | Minimal (Microsoft)    | Full (User)               |
| Cost               | Lower for web apps     | Higher for most workloads |
| Control            | Less                   | Full                      |

---

## 5. References

* [Microsoft: App Service vs. Virtual Machines](https://learn.microsoft.com/en-us/azure/app-service/overview)
* [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
* [Best practices for cloud apps](https://learn.microsoft.com/en-us/azure/architecture/best-practices/web-app)

