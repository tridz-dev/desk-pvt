<template>
	<div>
		<button
			@click="toggleAccordion()"
			class="flex items-center space-x-3 pl-[20px]"
			:aria-expanded="isOpen"
			:aria-controls="`collapse${_uid}`"
		>
			<CustomIcons
				:class="{
					'rotate-180': isOpen,
					'rotate-0': !isOpen,
				}"
				name="chevron-down-accordion"
			/>
			<slot name="title" />
		</button>

		<div
			class="flex justify-between w-[75%] pl-[20px]"
			v-show="isOpen"
			:id="`collapse${_uid}`"
		>
			<div>
				<slot class="flex-col" name="contact" />
			</div>
			<div>
				<slot name="email" />
			</div>
			<div>
				<slot name="phoneNo" />
			</div>
		</div>
		<div
			class="flex justify-between w-[75%] pl-[20px]"
			v-show="isOpen"
			:id="`collapse${_uid}`"
		>
			<div>
				<slot name="id" />
			</div>
			<div>
				<slot name="subject" />
			</div>
			<div>
				<slot name="status" />
			</div>
			<div>
				<slot name="ticketType" />
			</div>
			<div>
				<slot name="priority" />
			</div>
			<div>
				<slot name="ticketContact" />
			</div>
			<div>
				<slot name="photo" />
			</div>
		</div>

		<div v-show="isOpen" :id="`collapse${_uid}`">
			<slot name="content" />
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
