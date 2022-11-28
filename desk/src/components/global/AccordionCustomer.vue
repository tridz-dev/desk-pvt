<template>
	<div>
		<button
			@click="toggleAccordion()"
			class="flex py-2 items-center space-x-3 mx-5 py-2 px-4 bg-[#F9FAFA] rounded"
			:aria-expanded="isOpen"
			:aria-controls="`collapse${_uid}`"
		>
			<slot name="title" />
			<CustomIcons
				:class="{
					'rotate-180': isOpen,
					'rotate-180': !isOpen,
				}"
				name="chevron-down-accordion"
			/>
		</button>
		<div v-show="!isOpen" :id="`collapse${_uid}`">
			<slot name="contact" />
		</div>

		<div v-show="isOpen" :id="`collapse${_uid}`">
			<slot name="ticket" />
		</div>
	</div>
</template>

<script>
import CustomIcons from "@/components/desk/global/CustomIcons.vue"
export default {
	name: "Accordion",
	props: ["value"],
	components: {
		CustomIcons,
	},
	data() {
		return {
			isOpen: false,
		}
	},
	methods: {
		toggleAccordion() {
			this.isOpen = !this.isOpen
		},
	},
}
</script>
