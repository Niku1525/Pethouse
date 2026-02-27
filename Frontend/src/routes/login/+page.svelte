<script>
	import { fade, fly } from 'svelte/transition';
	import { onMount } from 'svelte';

	// svelte-ignore export_let_unused
		export let data;

	let email = '';
	let password = '';
	let showPassword = false;

	function handleLogin() {
		console.log('Intentando login:', { email, password });
	}
</script>

<section class="login-wrapper" in:fade>
	<div class="login-card px-4" in:fly={{ y: 30, duration: 400, opacity: 0 }}>
		<h2>Bienvenido</h2>
		<p class="subtitle">Inicia sesión para continuar</p>

		<form on:submit|preventDefault={handleLogin}>
			<div class="input-group">
				<!-- svelte-ignore a11y_label_has_associated_control -->
				<label>Correo electrónico</label>
				<input type="email" bind:value={email} placeholder="ejemplo@email.com" required />
			</div>

			<div class="input-group">
				<!-- svelte-ignore a11y_label_has_associated_control -->
				<label>Contraseña</label>

				<div class="password-wrapper">
					<input
						type={showPassword ? 'text' : 'password'}
						bind:value={password}
						placeholder="••••••••"
						required
					/>
					<!-- svelte-ignore a11y_click_events_have_key_events -->
					<!-- svelte-ignore a11y_no_static_element_interactions -->
					<span class="toggle-password" on:click={() => (showPassword = !showPassword)}>
						{showPassword ? '👁' : '👁‍🗨'}
					</span>
				</div>
			</div>

			<button class="btn-login">Iniciar Sesión</button>
		</form>

		<p class="footer-text">
			¿No tienes cuenta? <a href="/registro">Regístrate</a>
		</p>
	</div>
</section>

<style>
	.login-wrapper {
		min-height: 85vh;
		display: flex;
		justify-content: center;
		align-items: center;
		background: linear-gradient(135deg, #ecd75f, #b89a14);
		padding: 1rem;	}

	.login-card {
		background: white;
		padding:2rem;
		border-radius: 20px;
		width: 100%;
		max-width: 500px;
		box-shadow: 0 30px 60px rgba(0, 0, 0, 0.25);
		text-align: center;

	}

	.login-card h2 {
		font-weight: 700;
		margin-bottom: 0.5rem;
	}

	.subtitle {
		color: #6c757d;
		margin-bottom: 2rem;
	}

	.input-group {
		margin-bottom: 2.5rem;
		text-align: left;
	}

	.input-group label {
		font-size: 1rem;
		font-weight: 600;
		display: block;
		margin-bottom: 0.5rem;
	}

	.input-group input {
		width: 100%;
		padding: 0.3rem;
		border-radius: 12px;
		border: 1px solid #dfe1e2;
		transition: all 0.2s ease;
	}

	.input-group input:focus {
		border-color: #0d6efd;
		box-shadow: 0 0 0 3px rgba(13, 110, 253, 0.2);
		outline: none;
	}

	.password-wrapper {
	position: relative;
}

.password-wrapper input {
	padding-right: 87px; /* espacio para el icono */
}

.toggle-password {
	position: absolute;
	right: 6px;
	top: 50%;
	transform: translateY(-50%);
	cursor: pointer;
	font-size: 1rem;
	user-select: none;
	color: #6c757d;
	transition: 0.2s ease;
}

.toggle-password:hover {
	color: #b7b921;
}

	.btn-login {
		width: 100%;
		padding: 0.9rem;
		border-radius: 12px;
		border: none;
		background: linear-gradient(135deg, #ced121, #828a1b);
		color: rgb(253, 253, 247);
		font-weight: 600;
		cursor: pointer;
		transition: all 0.25s ease;
		box-shadow: 0 8px 20px rgba(13, 110, 253, 0.3);
	}

	.btn-login:hover {
		transform: translateY(-3px);
		box-shadow: 0 12px 30px rgba(13, 110, 253, 0.4);
	}

	.footer-text {
		margin-top: 1.5rem;
		font-size: 0.9rem;
		color: #6c757d;
	}

	.footer-text a {
		color: #0d6efd;
		text-decoration: none;
		font-weight: 600;
	}

	.footer-text a:hover {
		text-decoration: underline;
	}

	@media (max-width: 480px) {
		.login-card {
			padding: 2rem;
		}
	}
</style>
