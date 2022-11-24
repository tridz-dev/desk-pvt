<template>
	<div class="flex">
		<div class="w-full">
			<div
				class="pl-[20px] pr-[16px] pb-[20px] border-b-[1px] pt-[7px] flex justify-between"
			>
				<div v-if="editingTitle">
					<Input
						v-if="editingTitle"
						label="Customer Name"
						type="text"
						v-model="customer"
					/>
					<div class="font-light text-base">
						{{ values.domain }}
					</div>
				</div>
				<div v-else>
					<div class="font-medium text-2xl w-full">
						{{ values.organizationName }}
					</div>
					<div v-if="editingDomain">
						<Input
							v-if="editingDomain"
							label="Domain"
							type="text"
							v-model="values.domain"
						/>
					</div>
					<div v-else class="font-light text-base">
						{{ values.domain }}
					</div>
				</div>
				<div v-if="editingTitle || editingDomain">
					<Button
						class="mr-1"
						appearance="primary"
						@click="updateCustomer()"
						>Save</Button
					>
					<Button class="mr-1" appearance="secondary">Discard</Button>
				</div>
				<div v-else>
					<Dropdown
						class="ml-auto"
						placement="right"
						:button="{
							icon: 'edit',
							appearance: 'minimal',
							label: 'Edit Customer',
						}"
						:options="[
							{
								label: 'Edit Title',
								icon: 'edit',
								handler: () => (editingTitle = true),
							},
							{
								label: 'Edit Domain',
								icon: 'edit',
								handler: () => (editingDomain = true),
							},
						]"
					/>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="trash"
						@click="removeCustomer()"
						>Delete</Button
					>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="plus"
						@click="
							() => {
								showNewContactDialog = true
							}
						"
						>Add Contact</Button
					>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="plus"
						@click="
							() => {
								showNewTicketDialog = true
							}
						"
						>Add Ticket</Button
					>
				</div>
			</div>
			<div>
				<div>
					<Accordion class="w-full pt-[5px]">
						<template v-slot:title>
							<span class="font-medium text-lg">Contacts </span>
						</template>

						<template v-slot:contact>
							<div v-for="contact in this.contactList">
								{{ contact.name }}
							</div>
						</template>
						<template v-slot:email>
							<div v-for="contact in this.contactList">
								{{ contact.email_ids[0].email_id }}
							</div>
						</template>
						<template v-slot:phoneNo>
							<div v-for="contact in this.contactList">
								{{ contact.phone_nos[0].phone }}
							</div>
						</template>
					</Accordion>
				</div>
				<div>
					<Accordion class="w-full pt-[5px]">
						<template v-slot:title>
							<span class="font-medium text-lg">Tickets </span>
						</template>

						<template v-slot:id>
							<div v-for="ticket in this.ticketList">
								{{ ticket.name }}
							</div>
						</template>
						<template v-slot:subject>
							<div v-for="ticket in this.ticketList">
								<a>
									{{ ticket.subject }}
								</a>
							</div>
						</template>
						<template v-slot:status>
							<div v-for="ticket in this.ticketList">
								{{ ticket.status }}
							</div>
						</template>
						<template v-slot:ticketType>
							<div v-for="ticket in this.ticketList">
								{{ ticket.ticket_type }}
							</div>
						</template>
						<template v-slot:priority>
							<div v-for="ticket in this.ticketList">
								{{ ticket.priority }}
							</div>
						</template>
						<template v-slot:ticketContact>
							<div v-for="ticket in this.ticketList">
								{{ ticket.contact }}
							</div>
						</template>
						<template v-slot:photo>
							<div v-for="customer in this.customerList">
								{{ customer.image }}
							</div>
						</template>
					</Accordion>
				</div>
			</div>
		</div>
		<NewContactDialog
			v-model="showNewContactDialog"
			@contact-created="
				() => {
					showNewContactDialog = false
				}
			"
		/>
		<NewTicketDialog
			v-model="showNewTicketDialog"
			@close="showNewTicketDialog = false"
			@ticket-created="
				() => {
					showNewTicketDialog = false
				}
			"
		/>
	</div>
</template>

<script>
import { Dropdown } from "frappe-ui"
import { ref } from "vue"
import { Input } from "frappe-ui"
import Accordion from "@/components/global/Accordion.vue"
import CustomIcons from "@/components/desk/global/CustomIcons.vue"
import NewContactDialog from "@/components/desk/global/NewContactDialog.vue"
import NewTicketDialog from "@/components/desk/tickets/NewTicketDialog.vue"
export default {
	name: "CustomerInfo",
	props: ["customer"],
	components: {
		Accordion,
		Dropdown,
		CustomIcons,
		NewContactDialog,
		NewTicketDialog,
		Input,
	},

	data() {
		return {
			editingTitle: false,
			editingDomain: false,
			contactList: [],
			ticketList: [],
			showNewContactDialog: false,
			showNewTicketDialog: false,
		}
	},
	computed: {
		ticketDoc() {
			console.log(this.$resources.ticket.data)
			return this.$resources.ticket.data
		},
		contactDoc() {
			console.log(this.$resources.contact.data || null)
			return this.$resources.contact.data
		},
		customerDoc() {
			return this.$resources.organization.doc || null
		},
		values() {
			return {
				organizationName: this.customerDoc?.customer_name || null,
				domain: this.customerDoc?.domain || null,
				mobile: this.contactDoc?.email_id || null,
			}
		},
	},
	resources: {
		organization() {
			return {
				type: "document",
				doctype: "FD Customer",
				name: this.customer,
			}
		},

		contact() {
			return {
				method: "frappedesk.api.fdCustomer.get_contact",
				params: {
					doctype: "Contact",
					link_name: this.customer,
					fields: ["*"],
				},

				auto: true,
				onSuccess: (doc) => {
					this.contactList = doc
					return this.contactList
				},
			}
		},
		ticket() {
			return {
				method: "frappe.client.get_list",
				params: {
					doctype: "Ticket",
					fields: ["*"],
					filters: {
						customer: this.customer,
					},
				},
				auto: true,
				onSuccess: (doc) => {
					this.ticketList = doc
					return this.ticketList
				},
			}
		},
		deleteCustomer() {
			return {
				method: "frappe.client.delete",
				params: {
					doctype: "FD Customer",
					name: this.customer,
				},

				onSuccess: (event) => {
					console.log(event, "hello")
				},
				auto: true,
			}
		},
	},

	methods: {
		removeCustomer() {
			return this.$resources.deleteCustomer
		},
		updateCustomer() {
			this.$resources.organization.setValue.submit({
				customer_name: this.customer,
				domain: this.values.domain,
			})
		},
		updateUrlSlug() {
			let doc = this.customer
			if (
				!this.$route.params.slug ||
				this.$route.params.slug !== doc.slug
			) {
				this.$router.replace({
					name: "Customer",
					params: {
						...this.$route.params,
						slug: doc.slug,
					},
					query: this.$route.query,
				})
			}
		},
	},
}
</script>
