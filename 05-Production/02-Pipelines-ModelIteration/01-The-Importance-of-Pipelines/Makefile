PACKAGE_NAME=trainer
FILENAME=train

#----------------------------------
# LOCAL COMMANDS
#----------------------------------

create_package:
	-@mkdir ${PACKAGE_NAME}
	-@touch ${PACKAGE_NAME}/__init__.py
	-@touch ${PACKAGE_NAME}/pipeline.py
	-@touch ${PACKAGE_NAME}/tools.py

launch_pipeline:
	-@python -m ${PACKAGE_NAME}.${FILENAME}

clean:
	-@rm *.csv *.joblib

test_local:
	-@python test.py

