from ..operator.save_as_template_operator import SaveAsAppTemplateOperator


def menu_func_import(self, context):
    self.layout.operator(
        SaveAsAppTemplateOperator.bl_idname, text="Save as App Template")