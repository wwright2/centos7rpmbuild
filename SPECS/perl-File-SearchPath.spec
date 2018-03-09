%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-File-SearchPath
Version:        0.07
Release:        1%{?dist}
Summary:        Search for a file in an environment variable path
License:        GPL+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-SearchPath/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/T/TJ/TJENNESS/File-SearchPath-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(Env::Path)
Requires:       perl(File::Spec) >= 0.8

%description
This module provides the ability to search a path-like environment variable
for a file (that does not necessarily have to be an executable).

%prep
%setup -q -n File-SearchPath-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.07-1
- Specfile autogenerated by cpanspec 1.78.
