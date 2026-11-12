<?php
/**
 * Shared .env loader and environment variable helper for Hetxa BOS.
 */
if (!defined('HETXA_ENV_LOADED')) {
    define('HETXA_ENV_LOADED', true);
    $envFile = dirname(__DIR__) . '/.env';
    if (file_exists($envFile)) {
        $envLines = @file($envFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) ?: [];
        foreach ($envLines as $envLine) {
            $envLine = trim($envLine);
            if ($envLine === '' || strpos($envLine, '#') === 0) continue;
            $envParts = explode('=', $envLine, 2);
            if (count($envParts) === 2) {
                $eKey = trim($envParts[0]);
                $eVal = trim($envParts[1]);
                if (preg_match('/^(["\'])(.*)\1$/', $eVal, $eMatch)) {
                    $eVal = $eMatch[2];
                }
                if (!isset($_ENV[$eKey])) {
                    $_ENV[$eKey] = $eVal;
                    putenv("$eKey=$eVal");
                }
            }
        }
    }
}

if (!function_exists('get_env_val')) {
    function get_env_val($key, $default = null) {
        $val = $_ENV[$key] ?? getenv($key);
        if ($val === false || $val === null || $val === '') {
            return $default;
        }
        $lower = strtolower((string)$val);
        if ($lower === 'true') return true;
        if ($lower === 'false') return false;
        return $val;
    }
}

