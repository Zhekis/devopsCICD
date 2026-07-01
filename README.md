Cloud-Native CI/CD pipeline with automated deployment to Kubernetes.

### ✅ Completed Tasks

- Python HTTP server application
- Unit tests (pytest)
- Dockerfile
- GitHub Actions CI (lint, test, build)
- Kubernetes manifests (Deployment + Service)
- GitHub Actions CD (build + push to Docker Hub)
- ArgoCD installation and GitHub integration
- Full CI/CD workflow

---

## 📁 Project Structure
```
devopsCICD/
├── .github/
│   └── workflows/
│       ├── cicd.yml
│       ├── release.yml
│       └── devops_course_pipeline.yml
├── k8sManifests/
│   └── devops.yml
├── server/
│   ├── application.py
│   ├── dockerfile
│   ├── index.html
│   └── test_application.py
├── requirements.txt
└── README.md
```
# Отчет:
Автоматический деплой в Kubernetes
---
🔄 Workflow

   <img width="4877" height="231" alt="deepseek_mermaid_20260701_fd3054" src="https://github.com/user-attachments/assets/c5eef099-da35-4c85-8ee7-a92df723d889" />

образ в докерхаб:

<img width="586" height="405" alt="image" src="https://github.com/user-attachments/assets/060e9cf2-05f9-4ef2-8703-0dad0cc9b623" />

Приложение установлено на контроль ArgoCD:

<img width="347" height="270" alt="image" src="https://github.com/user-attachments/assets/9024797e-6413-4e37-9e9e-6f1401354006" />
<img width="1270" height="430" alt="image" src="https://github.com/user-attachments/assets/9a512d78-1f0e-4a7d-8fab-6244b3003756" />

---

В результате работы был создан полноценный Cloud-Native CI/CD пайплайн с использованием современного инструментария:

✅ GitHub Actions — автоматизация сборки и тестирования

✅ Docker — контейнеризация приложения

✅ Docker Hub — хранение образов

✅ Kubernetes — оркестрация контейнеров

✅ ArgoCD — GitOps деплой

✅ Minikube — локальный кластер

Пайплайн обеспечивает:

Автоматическую сборку при каждом push

Автоматическое тестирование

Публикацию образов

Обновление манифестов с датой релиза


📊 Проверка

kubectl get pods -n devops

http://127.0.0.1:12345

<img width="145" height="39" alt="image" src="https://github.com/user-attachments/assets/9609a4de-783c-4d28-a619-2e9662e9d738" />

--- 


📁 Ссылки
[GitHub Repository] - https://github.com/zhekis/devopsCICD

Docker Hub: https://hub.docker.com/r/zhekis/devops

ArgoCD UI: https://172.22.44.225
