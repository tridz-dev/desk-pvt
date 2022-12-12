import frappe

@frappe.whitelist()
def get_ticket_count():
    ticket_count = frappe.db.get_list('Ticket',fields=['count(name) as count','creation'],group_by='creation')


    return ticket_count

@frappe.whitelist()
def ticket_status():
    ticket_count_by_status = frappe.db.get_list('Ticket',fields=['count(name) as count','status','creation','resolution_date','opening_date','first_responded_on','modified'],group_by='status')
    
    return ticket_count_by_status

@frappe.whitelist()
def ticket_type():                                                                                                      
    ticket_count_by_type= frappe.db.get_list('Ticket',fields=['count(name) as count','ticket_type'],group_by='ticket_type')

    return ticket_count_by_type

@frappe.whitelist()
def average_first_response_time():
    average_response_time = float(0.0)
    ticket_list = frappe.get_list('Ticket', fields=['name','first_response_time'],filters={'first_response_time':['not like','']})

    for ticket in ticket_list:
        average_response_time +=ticket.first_response_time

    return ((average_response_time)/len(ticket_list))/3600

@frappe.whitelist()
def average_resolution_time():
    average_resolution_time = float(0.0)
    ticket_list = frappe.get_list('Ticket', fields=['name','resolution_time'],filters={'resolution_time':['not like','']})

    for ticket in ticket_list:
        average_resolution_time += ticket.resolution_time

    return ((average_resolution_time)/len(ticket_list))/3600

# def resolution_within_sla():
#     ticket_list = frappe.get_list('Ticket', fields=['name','agreement_status','sla','resolution_by','priority'])

#     for ticket in ticket_list:
#         sla_doc = frappe.db.get_list('Service Level Priority',fields=['resolution_time'],filters={'parent':ticket.sla})
