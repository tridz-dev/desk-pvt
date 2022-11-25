<template>
	<div class="flex">
		<div class="w-full">
			<div
				class="pl-[20px] pr-[16px] pb-[20px] border-b-[1px] pt-[7px] flex justify-between"
			>
				<div v-if="editingTitle">
					<div>
						<Input
							label="Customer Name"
							type="text"
							v-model="customer"
						/>
					</div>
					<div>
						<Input
							label="Domain"
							type="text"
							v-model="values.domain"
						/>
					</div>
				</div>
				<div v-else>
					<div class="flex">
						<div
							class="bg-[#90C5F4] w-14 h-14 justify-center flex items-center rounded-md font-medium text-white text-2xl"
						>
							<span>{{ acronym[0] }} {{ acronym[1] }}</span>
						</div>
						<div class="pl-4">
							<div class="font-medium text-2xl w-full">
								{{ values.organizationName }}
							</div>

							<div class="font-light text-base">
								{{ values.domain }}
							</div>
						</div>
					</div>
				</div>
				<div v-if="editingTitle">
					<Button
						class="mr-1"
						appearance="primary"
						@click="
							() => {
								updateCustomer()
								editingTitle = false
							}
						"
						>Save</Button
					>
					<Button
						class="mr-1"
						appearance="secondary"
						@click="
							() => {
								editingTitle = false
								$resources.organization.reload()
							}
						"
						>Discard</Button
					>
				</div>
				<div v-else>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="edit"
						@click="editingTitle = true"
						>Edit</Button
					>
					<Button
						class="mr-1"
						appearance="secondary"
						icon-left="trash"
						@click="deleteCustomer()"
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
				<Accordion class="w-full pt-[5px]">
					<template v-slot:title>
						<span class="font-medium text-lg"
							>Contacts ({{
								customerDoc.contact_count == null
									? "0"
									: customerDoc.contact_count
							}})
						</span>
					</template>

					<template
						v-slot:contact
						v-for="contact in this.contactList"
					>
						<div class="flex justify-between w-[75%]">
							<div>
								{{ contact.name }}
							</div>
							<div>
								{{ contact.email_ids[0].email_id }}
							</div>
							<div>
								{{ contact.phone_nos[0].phone }}
							</div>
						</div>
					</template>
				</Accordion>
			</div>
			<div>
				<Accordion class="w-full pt-[5px]">
					<template v-slot:title>
						<span class="font-medium text-lg"
							>Tickets ({{
								customerDoc.ticket_count == null
									? "0"
									: customerDoc.ticket_count
							}})
						</span>
					</template>

					<template v-slot:ticket v-for="ticket in this.ticketList">
						<div class="font-normal text-sm text-[#74808B]">
							{{ ticket.name }}
						</div>

						<div class="font-semibold text-sm text-[#192734]">
							<a>
								{{ ticket.subject }}
							</a>
						</div>

						<div class="font-normal text-xs">
							{{ ticket.status }}
						</div>

						<div class="font-medium text-xs">
							{{ ticket.ticket_type }}
						</div>

						<div class="font-normal text-xs text-[#74808B]">
							{{ ticket.priority }}
						</div>

						<div class="font-normal text-sm text-[#74808B]">
							{{ ticket.contact }}
						</div>

						<div>
							{{ customer.image }}
						</div>
					</template>
				</Accordion>
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
			contactList: [],
			ticketList: [],
			showNewContactDialog: false,
			showNewTicketDialog: false,
		}
	},
	computed: {
		acronym() {
			var str = this.$resources.organization.doc.customer_name
			var matches = str.match(/\b(\w)/g)
			var acronym = matches.join("")
			return acronym
		},
		ticketDoc() {
			return this.$resources.ticket.data
		},
		contactDoc() {
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
	},

	methods: {
		deleteCustomer() {
			return {
				method: "frappe.client.delete",
				params: {
					doctype: "FD Customer",
					name: this.customer,
				},
				auto: true,

				onSuccess: () => {
					this.$toast({
						title: "Customer deleted",
						customIcon: "circle-check",
						appearance: "success",
					})
					this.resetForm()
				},

				onError: (e) => {
					console.log(e)
					this.$toast({
						title: "Cannot delete customer",
						text: e,
						customIcon: "circle-fail",
						appearance: "danger",
					})
				},
			}
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
