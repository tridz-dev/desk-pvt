<template>
	<div class="flex">
		<div class="w-full">
			<div
				class="pl-[20px] pr-[16px] pb-[20px] pt-[7px] flex justify-between"
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
								{{ values.customerName }}
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
								$resources.customer.reload()
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
				<AccordionCustomer class="w-full pt-[5px] pb-3 pl">
					<template v-slot:title>
						<span class="font-medium text-lg ml-[16px]"
							>Contacts ({{
								customerDoc.contact_count == null
									? "0"
									: customerDoc.contact_count
							}})
						</span>
					</template>

					<template v-slot:contact>
						<div
							v-for="contact in contactDoc"
							class="flex pl-[22px] font-normal text-sm py-3 border-b border-[#F4F5F6]-200 mx-5"
						>
							<div class="w-[30%]">
								<router-link
									:to="`/frappedesk/contacts/${contact.name}`"
								>
									{{ contact.name }}
								</router-link>
							</div>
							<div class="w-[20%]">
								{{ contact.email_ids[0].email_id }}
							</div>
							<div class="w-[20%]">
								{{
									contact.phone_nos.length == 0
										? ""
										: contact.phone_nos[0].phone
								}}
							</div>
						</div>
					</template>
				</AccordionCustomer>
			</div>
			<div>
				<AccordionCustomer class="w-full pt-[5px]">
					<template v-slot:title>
						<span class="font-medium text-lg ml-[16px]"
							>Tickets ({{
								customerDoc.ticket_count == null
									? "0"
									: customerDoc.ticket_count
							}})
						</span>
					</template>

					<template v-slot:ticket>
						<div
							v-for="ticket in ticketDoc"
							class="flex w-[100%] pl-[22px] font-normal text-sm py-3 mx-5"
						>
							<div
								class="font-normal w-[10%] text-sm text-[#74808B]"
							>
								{{ ticket.name }}
							</div>

							<div
								class="w-[40%] font-semibold text-sm text-[#192734]"
							>
								<router-link
									:to="`/frappedesk/tickets/${ticket.name}`"
								>
									{{ ticket.subject }}
								</router-link>
							</div>

							<div
								class="w-[10%] font-normal text-xs"
								:class="getStatusStyle(ticket.status)"
							>
								{{ ticket.status }}
							</div>

							<div
								class="w-[10%] font-medium text-xs"
								:class="getTypeStyle(ticket.ticket_type)"
							>
								{{ ticket.ticket_type }}
							</div>

							<div
								class="w-[10%] font-normal text-xs text-[#74808B]"
							>
								{{ ticket.priority }}
							</div>

							<div
								class="w-[10%] font-normal text-sm text-[#74808B]"
							>
								{{ ticket.contact }}
							</div>

							<!-- <Avatar
									v-for="contact in contactDoc"
									:label="user"
									:imageURL="contact.image"
									size="md"
								/> -->
						</div>
					</template>
				</AccordionCustomer>
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
import { Dropdown, Avatar } from "frappe-ui"
import { ref, toRaw } from "vue"
import { Input } from "frappe-ui"
import AccordionCustomer from "@/components/global/AccordionCustomer.vue"
import CustomIcons from "@/components/desk/global/CustomIcons.vue"
import NewContactDialog from "@/components/desk/global/NewContactDialog.vue"
import NewTicketDialog from "@/components/desk/tickets/NewTicketDialog.vue"
export default {
	name: "CustomerInfo",
	props: ["customer"],
	components: {
		Dropdown,
		CustomIcons,
		NewContactDialog,
		NewTicketDialog,
		Input,
		Avatar,
		AccordionCustomer,
	},

	data() {
		return {
			editingTitle: false,
			showNewContactDialog: false,
			showNewTicketDialog: false,
		}
	},
	computed: {
		acronym() {
			var str = this.$resources.customer.doc.customer_name
			var matches = str.match(/\b(\w)/g)
			var acronym = matches.join("")
			return acronym
		},
		ticketDoc() {
			return this.$resources.ticket.data
		},
		contactDoc() {
			console.log(toRaw(this.$resources.contact.data, "bro"))
			return this.$resources.contact.data
		},
		customerDoc() {
			return this.$resources.customer.doc || null
		},
		values() {
			return {
				customerName: this.customerDoc?.customer_name || null,
				domain: this.customerDoc?.domain || null,
				mobile: this.contactDoc?.email_id || null,
			}
		},
	},
	resources: {
		customer() {
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
			}
		},
	},

	methods: {
		deleteCustomer() {
			return this.$resources.customer.delete.submit(null, {
				onSuccess: () => {
					this.$toast({
						title: "Customer deleted",
						customIcon: "circle-check",
						appearance: "success",
					})
					this.resetForm()
				},
				auto: true,

				onError: (e) => {
					console.log(e)
					this.$toast({
						title: "Cannot delete customer",
						text: e,
						customIcon: "circle-fail",
						appearance: "danger",
					})
				},
			})
		},
		updateCustomer() {
			this.$resources.customer.setValue.submit({
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
		getStatusStyle(status) {
			const color = {
				Open: "#38A160",
				Replied: "#FF7C36",
				Resolved: "#E24C4C",
				Closed: "#E24C4C",
			}[status]
			return `border-[${color}] text-[${color}]`
		},

		getTypeStyle(ticket_type) {
			const color = {
				Question: "#B7B6FC",
				Bug: "#E24C4C",
				Incident: "#FF7C36",
			}[ticket_type]
			return `border-[${color} text-[${color}]]`
		},
	},
}
</script>
