import java.net.URI

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.kapt)
    alias(libs.plugins.hilt)
}

fun apiUrl(name: String, fallback: String): String {
    val value = providers.gradleProperty(name).orElse(fallback).get()
    val uri = URI(value)
    require(uri.host != null && uri.userInfo == null && uri.query == null && uri.fragment == null)
    require(value.endsWith("/")) { "$name must end in /" }
    require(uri.scheme == "https" || (name == "DEV_API_URL" && uri.scheme == "http"))
    return "\"$value\""
}

android {
    namespace = "app.romear"
    compileSdk = 36
    buildToolsVersion = "36.0.0"
    defaultConfig {
        applicationId = "app.romear"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "0.0.1"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        buildConfigField("boolean", "ALLOW_TEST_DATA", "false")
    }
    // dev is the standard debug build. Staging/prod use release optimizations and no debug bypass.
    buildTypes {
        debug {
            applicationIdSuffix = ".dev"
            versionNameSuffix = "-dev"
            buildConfigField("String", "ENVIRONMENT", "\"dev\"")
            buildConfigField("String", "API_BASE_URL", apiUrl("DEV_API_URL", "https://romear-api.onrender.com/"))
            manifestPlaceholders["cleartextAllowed"] = "true"
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            buildConfigField("String", "ENVIRONMENT", "\"prod\"")
            buildConfigField("String", "API_BASE_URL", apiUrl("PROD_API_URL", "https://romear-api.onrender.com/"))
            manifestPlaceholders["cleartextAllowed"] = "false"
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
        create("staging") {
            initWith(getByName("release"))
            applicationIdSuffix = ".staging"
            versionNameSuffix = "-staging"
            matchingFallbacks += "release"
            buildConfigField("String", "ENVIRONMENT", "\"staging\"")
            buildConfigField("String", "API_BASE_URL", apiUrl("STAGING_API_URL", "https://romear-api.onrender.com/"))
        }
    }
    buildFeatures { viewBinding = true; buildConfig = true }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    testOptions { unitTests.isReturnDefaultValues = true }
    lint { abortOnError = true; checkReleaseBuilds = true }
}

kotlin { compilerOptions { jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17) } }

kapt { correctErrorTypes = true }

dependencies {
    implementation(libs.androidx.core)
    implementation(libs.androidx.appcompat)
    implementation(libs.androidx.fragment)
    implementation(libs.androidx.navigation)
    implementation(libs.androidx.lifecycle.viewmodel)
    implementation(libs.androidx.lifecycle.runtime)
    implementation(libs.material)
    implementation(libs.constraintlayout)
    implementation(libs.coroutines)
    implementation(libs.retrofit)
    implementation(libs.retrofit.gson)
    implementation(libs.okhttp)
    implementation(libs.hilt)
    kapt(libs.hilt.compiler)
    testImplementation(libs.junit)
    testImplementation(libs.coroutines.test)
    testImplementation(libs.mockwebserver)
    androidTestImplementation(libs.androidx.test.runner)
    androidTestImplementation(libs.androidx.test.junit)
    androidTestImplementation(libs.espresso)
}
