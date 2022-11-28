<template>
	<div>
		<button
			@click="toggleAccordion()"
			class="flex items-center w-full space-x-3 pl-[20px] bg-[#F9FAFA]"
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
