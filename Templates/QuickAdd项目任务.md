---
name: 项目任务
description: 创建项目任务清单
---

# 📋 {{title}}

**项目开始**: {{date:YYYY-MM-DD}}
**预计完成**: 
**状态**: 🟡 进行中

## 📝 项目目标


## 🎯 关键里程碑

### 里程碑 1
- [ ] 

### 里程碑 2
- [ ] 

### 里程碑 3
- [ ] 

---

## 📋 任务清单

### 🔥 高优先级
- [ ] 

### ⚡ 中优先级
- [ ] 

### 📌 低优先级
- [ ] 

---

## 📊 进度追踪
```dataview
TABLE without ID
  file.tasks.where(t => !t.completed).length as "待办",
  file.tasks.where(t => t.completed).length as "完成",
  round(file.tasks.where(t => t.completed).length * 100 / file.tasks.length, 1) + "%" as "进度"
WHERE file.link = [[{{title}}]]
```

---

## 📝 笔记与想法


## 🔗 相关链接
- 

---
**创建时间**: {{date:YYYY-MM-DD HH:mm}}
**更新时间**: {{date:YYYY-MM-DD HH:mm}}
