PACKAGE_NAME=trainer
FILENAME=task

#----------------------------------
# LOCAL COMMANDS
#----------------------------------

create_package:
	-@mkdir ${PACKAGE_NAME}
	-@touch ${PACKAGE_NAME}/__init__.py
	-@touch ${PACKAGE_NAME}/pipeline.py
	-@touch ${PACKAGE_NAME}/tools.py

train_simple_model:
	-@python first_model.py

clean:
	-@rm *.csv *.joblib

test_local:
	-@python test.py

