from odoo import api, fields, models, _


class inherit_res(models.Model):
	_inherit = 'res.partner'


	document = fields.Binary(string="Documents")
	tasks = fields.Many2many('project.task', 'task_users_rel', 'name','project_id', 'Tasks')


	@api.onchange('tasks')
	def _compute_tasks(self):
		project_obj = self.env['res.partner'].search([('user_ids','=', self.env.uid)])
		print(project_obj)
		for line in project_obj:
			obj = self.env['project.task'].browse(line.id)
			print(obj)
			t = obj.name
			print(t)

			#print(line.name, line.user_id.id)
			#partner_obj = self.env['res.users'].browse(line.user_id.id)
			#print(partner_obj)
			#if line.user_id.id == self.env.uid:
				#print('inside if ')
			


		'''user_obj = self.env['res.users'].search([])
		print(user_obj)
		for line in user_obj:
			print(line.id, line.name)
		#active_user = self.env.uid
		#print(active_user)

			task_obj = self.env['project.task'].browse(line.user_id.id)
			print(task_obj)
			if line.id == self.env.uid :
				
				print(line.tasks)'''







			



			