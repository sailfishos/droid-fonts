%global fontname droid

# %%_font_pkg can't handle wildcards. Only use one line per list.
%global sans_fonts DroidSans.ttf DroidSans-Bold.ttf DroidSansFallback.ttf DroidSansJapanese.ttf DroidSansArabic.ttf DroidSansHebrew.ttf DroidSansThai.ttf
%global serif_fonts DroidSerif-Bold.ttf DroidSerif-BoldItalic.ttf DroidSerif-Italic.ttf DroidSerif-Regular.ttf
%global sans_mono_fonts DroidSansMono.ttf

%global sans_conf 55-%{fontname}-sans.conf
%global serif_conf 55-%{fontname}-serif.conf
%global sans_mono_conf 55-%{fontname}-sans-mono.conf

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text.

Name:    %{fontname}-fonts
# The font files all have the same version except for sans fallback which I'm going to ignore here
Version: 1.0.115_20251012
Release: 1
Summary: General-purpose fonts released by Google as part of Android
License:   ASL 2.0
URL:       https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/data/fonts/
Source0:   droid-fonts-1.0.113_20100701.tar.xz
Source9:   NOTICE
Source10:  README.txt
Source11:  %{name}-sans-fontconfig.conf
Source12:  %{name}-sans-mono-fontconfig.conf
Source13:  %{name}-serif-fontconfig.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-1.0.113_20100701-%{release}-XXXXXX)

BuildArch:     noarch
BuildRequires: fontpackages-devel

%description
%common_desc

%package -n %{fontname}-sans-fonts
Summary:   A humanist sans serif typeface
Provides:  scalable-font-ja
Provides:  scalable-font-zh-TW
Provides:  scalable-font-zh-HK
Provides:  scalable-font-zh-CN
Provides:  scalable-font-zh-SG
Provides:  scalable-font-zh-MO
Requires:  fontpackages-filesystem
Obsoletes: %{name}-common

%description -n %{fontname}-sans-fonts
%common_desc

Droid Sans is a humanist sans serif typeface designed for user interfaces and
electronic communication.

%_font_pkg -n sans -f %{sans_conf} %{sans_fonts}

%package -n %{fontname}-sans-mono-fonts
Summary:  A humanist monospace sans serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-sans-mono-fonts
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%_font_pkg -n sans-mono -f %{sans_mono_conf} %{sans_mono_fonts}
%doc *.txt

%package -n %{fontname}-serif-fonts
Summary:  A contemporary serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-serif-fonts
%common_desc

Droid Serif is a contemporary serif typeface family designed for comfortable
reading on screen. Droid Serif is slightly condensed to maximize the amount of
text displayed on small screens. Vertical stress and open forms contribute to
its readability while its proportion and overall design complement its
companion Droid Sans.

%_font_pkg -n serif -f %{serif_conf} %{serif_fonts}

%prep
%setup -q -n %{name}-1.0.113_20100701
install -m 0644 -p %{SOURCE9}  notice.txt
install -m 0644 -p %{SOURCE10} readme.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir}/ %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{sans_conf}
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{sans_mono_conf}
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontconfig_templatedir}/%{serif_conf}

ln -sf %{_fontconfig_templatedir}/%{sans_conf}      %{buildroot}%{_fontconfig_confdir}/
ln -sf %{_fontconfig_templatedir}/%{sans_mono_conf} %{buildroot}%{_fontconfig_confdir}/
ln -sf %{_fontconfig_templatedir}/%{serif_conf}     %{buildroot}%{_fontconfig_confdir}/
