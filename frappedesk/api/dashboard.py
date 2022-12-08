import frappe

@frappe.whitelist()
def get_ticket_count(from_date,to_date):
    ticket_count = frappe.db.count('Ticket', filters = [['creation','between',[from_date,to_date]]])

    return ticket_count

@frappe.whitelist()
def ticket_status(from_date,to_date):
    ticket_count_by_status = frappe.db.get_list('Ticket',filters = [['creation','between',[from_date,to_date]]],fields=['count(name) as count','status'],group_by='status')
    
    return ticket_count_by_status

@frappe.whitelist()
def ticket_type(from_date,to_date):
    ticket_count_by_type= frappe.db.get_list('Ticket',filters = [['creation','between',[from_date,to_date]]],fields=['count(name) as count','ticket_type'],group_by='ticket_type')

    return ticket_count_by_type