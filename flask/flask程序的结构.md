## 大型程序的结构

Flask并不强求大型项目使用特定的组织方式，程序结构的组织方式完全由开发者决定。

### 项目结构

基本结构如下：

```shell
|-flasky
	|-app/
		|-templates/
		|-static/
		|-main/
			|-__init__.py
			|-errors.py
			|-forms.py
			|-views.py
		|-__init__.py
		|-email.py
		|-models.py
	|-migrations/
	|-tests/
		|-__init__.py
		|-test*.py
	|-venv/
	|-requirements.txt
	|-config.py
	|-manage.py
```

这种结构有四个顶级文件夹：

- Flask程序一般都保存在名为app的包中
- 和之前一样，migrations文件夹包含数据库迁移脚本
- 单元测试编写在tests包中
- 和之前一样，venv文件夹包含Python虚拟环境。

同时还创建了一些新文件：

- requirements.txt列出了所有依赖包，便于在其他电脑中重新生成相同的虚拟环境；
- config.py存储配置；
- manage.py用于启动程序以及其他的程序任务；
