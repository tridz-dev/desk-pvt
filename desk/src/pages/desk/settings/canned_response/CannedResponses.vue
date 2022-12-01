<template>
	<div class="flex flex-col h-full px-4">
		<ListManager
			ref="cannedResponseList"
			:options="{
				cache: ['Canned Response', 'Desk'],
				doctype: 'Canned Response',
				fields: ['title', 'owner'],
				urlQueryFilters: true,
				saveFiltersLocally: true,
				limit: 20,
			}"
		>
			<template #body>
				<ListViewer
					:options="{
						base: '12',
						filterBox: true,
						presetFilters: true,
						fields: {
							title: {
								label: 'Title',
								width: '6',
							},
							owner: {
								label: 'Author',
								width: '6',
							},
						},
					}"
					class="text-base h-[100vh] pt-4"
					@add-item="
						() => {
							showNewCannedResponsesDialog = true
						}
					"
				>
					<template #field-title="{ row }">
						<router-link
							:to="{
								path: `/frappedesk/settings/canned_responses/${row.name}`,
							}"
						>
							{{ `${row.title}` }}
						</router-link>
					</template>
				</ListViewer>
			</template>
		</ListManager>
		<AddNewCannedResponsesDialog
			v-model="showNewCannedResponsesDialog"
			@close="
				() => {
					showNewCannedResponsesDialog = false
				}
			"
		/>
	</div>
</template>
<script>
import { inject, ref } from "vue"
import CannedResponseList from "@/components/desk/settings/canned_responses/CannedResponseList.vue"
import ListManager from "@/components/global/ListManager.vue"
import ListViewer from "@/components/global/ListViewer.vue"
import AddNewCannedResponsesDialog from "@/components/desk/global/AddNewCannedResponsesDialog.vue"
export default {
	name: "Canned Responses",
	components: {
		CannedResponseList,
		ListManager,
		ListViewer,
		AddNewCannedResponsesDialog,
	},

	data() {
		return {
			showNewCannedResponsesDialog: false,
		}
	},
	setup() {
		const showNewCannedResponsesDialog = ref(false)
		return {
			showNewCannedResponsesDialog,
		}
	},
	mounted() {
		// this.$event.emit("set-selected-setting", "Canned Responses")
		// this.$event.emit("show-top-panel-actions-settings", "CannedResponses")s
		// this.$event.on("show-new-canned_response-dialog", () => {
		// 	this.showNewCannedResponsesDialog = true
		// })
		this.$event.on("delete-selected-canned_responses", () => {
			this.$resources.bulk_delete_responses.submit({
				items: Object.keys(
					this.$refs.listManager.manager.selectedItems
				),
				doctype: "Canned Response",
			})
		})
	},
	unmounted() {
		// this.$event.off("show-new-canned_response-dialog")
		this.$event.off("delete-selected-canned_responses")
	},
	resources: {
		bulk_delete_responses() {
			return {
				method: "frappedesk.api.doc.delete_items",
				onSuccess: () => {
					this.$router.go()
				},
				onError: (err) => {
					this.$refs.listManager.manager.reload()
					this.$toast({
						title: "Error while deleting canned responses",
						text: err,
						customIcon: "circle-check",
						appearance: "success",
					})
					// this.$event.emit(
					// 	"show-top-panel-actions-settings",
					// 	"CannedResponses"
					// )
				},
			}
		},
	},
}
</script>
