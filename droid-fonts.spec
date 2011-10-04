%global fontname droid

%global common_desc \
The Droid typeface family was designed in the fall of 2006 by Ascender's \
Steve Matteson, as a commission from Google to create a set of system fonts \
for its Android platform. The goal was to provide optimal quality and comfort \
on a mobile handset when rendered in application menus, web browsers and for \
other screen text.

Name:    %{fontname}-fonts
# The font files all have the same version except for sans fallback which I'm going to ignore here
Version: 1.0.113_20100701
Release: 1
Summary: General-purpose fonts released by Google as part of Android

Group:     User Interface/X
License:   ASL 2.0
URL:       http://android.git.kernel.org/?p=platform/frameworks/base.git;a=tree;f=data/fonts
Source0:   droid-fonts-%{version}.tar.xz
Source9:   NOTICE
Source10:  README.txt
Source11:  %{name}-sans-fontconfig.conf
Source12:  %{name}-sans-mono-fontconfig.conf
Source13:  %{name}-serif-fontconfig.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

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

# can't use wildcard for Sans fonts since we also have `SansMono'
%_font_pkg -n sans -f ??-%{fontname}-sans.conf DroidSans.ttf DroidSans-Bold.ttf DroidSansFallback.ttf DroidSansJapanese.ttf DroidSansArabic.ttf DroidSansHebrew.ttf DroidSansThai.ttf


%package -n %{fontname}-sans-mono-fonts
Summary:  A humanist monospace sans serif typeface
Requires: fontpackages-filesystem

%description -n %{fontname}-sans-mono-fonts
%common_desc

Droid Sans Mono is a humanist monospace sans serif typeface designed for user
interfaces and electronic communication.

%_font_pkg -n sans-mono -f ??-%{fontname}-sans-mono.conf DroidSansMono.ttf
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

%_font_pkg -n serif -f ??-%{fontname}-serif.conf DroidSerif*ttf


%prep
%setup -q
install -m 0644 -p %{SOURCE9}  notice.txt
install -m 0644 -p %{SOURCE10} readme.txt


%build


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/55-%{fontname}-sans.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/55-%{fontname}-sans-mono.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/55-%{fontname}-serif.conf

for fontconf in 55-%{fontname}-sans.conf \
                55-%{fontname}-sans-mono.conf \
                55-%{fontname}-serif.conf ; do
  ln -s %{_fontconfig_templatedir}/$fontconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done


%clean
rm -fr %{buildroot}
