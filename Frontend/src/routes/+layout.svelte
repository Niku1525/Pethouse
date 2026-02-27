<script>
	import 'bootstrap/dist/css/bootstrap.min.css';
	import { onMount } from 'svelte';
	import Navbar from '$lib/components/Navbar.svelte';
	import '../app.css';

	onMount(async () => {
		await import('bootstrap/dist/js/bootstrap.bundle.min.js');
	});
</script>

<Navbar />
<slot />
