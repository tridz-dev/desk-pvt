<template>
	<div class="flex">
		<div class="w-full">
			<div
				class="pl-[20px] pr-[16px] pb-[20px] border-b-[1px] pt-[7px] flex justify-between"
			>
				<div>
					<div class="font-medium text-2xl w-full">
						{{ values.organizationName }}
					</div>
					<div class="font-light text-base">
						{{ values.domain }}
					</div>
				</div>
				<div>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="edit-2"
					>
						Edit
					</Button>
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

						<template v-slot:customer>
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
							<span class="font-medium text-lg">Contacts </span>
						</template>

						<template v-slot:customer>
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
import { ref } from "vue"
import Accordion from "@/components/global/Accordion.vue"
import CustomIcons from "@/components/desk/global/CustomIcons.vue"
import NewContactDialog from "@/components/desk/global/NewContactDialog.vue"
import NewTicketDialog from "@/components/desk/tickets/NewTicketDialog.vue"
export default {
	name: "CustomerInfo",
	props: ["customer"],
	components: {
		Accordion,
		CustomIcons,
		NewContactDialog,
		NewTicketDialog,
	},

	data() {
		return {
			contactList: [],
			ticketList: [],
			showNewContactDialog: false,
			showNewTicketDialog: false,
		}
	},
	computed: {
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

				onError: (e) => {
					console.log(e)
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
	},
}
</script>
