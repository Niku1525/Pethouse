<script>
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';
	import '../../app.css';

	let scrolled = false;

	onMount(() => {
		const handleScroll = () => {
			scrolled = window.scrollY > 30;
		};

		window.addEventListener('scroll', handleScroll);
		return () => window.removeEventListener('scroll', handleScroll);
	});
</script>

<nav
	in:fly={{ y: -60, duration: 600 }}
	class="navbar navbar-expand-lg fixed-top {scrolled ? 'navbar-scrolled' : 'navbar-top'}"
>
	<div class="container">

		<!-- Logo -->
		<a class="navbar-brand brand-logo" href="/">
			PetHouse
		</a>

		<button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarNav"
		>
			<span class="navbar-toggler-icon"></span>
		</button>

		<div class="collapse navbar-collapse justify-content-end" id="navbarNav">
			<ul class="navbar-nav align-items-center">
				<li class="nav-item">
					<a class="nav-link nav-custom" href="/">Inicio</a>
				</li>

				<li class="nav-item">
					<a class="nav-link nav-custom" href="/adoptar">Adoptar</a>
				</li>

				<li class="nav-item">
					<a class="nav-link nav-custom" href="/rastreador">Rastreador</a>
				</li>

				<li class="nav-item ms-3">
					<a class="btn btn-login" href="/login">Login</a>
				</li>
			</ul>
		</div>
	</div>
</nav>
