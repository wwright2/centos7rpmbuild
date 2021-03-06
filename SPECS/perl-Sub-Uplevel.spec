%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Sub-Uplevel
Version:        0.2800
Release:        1%{?dist}
Summary:        Apparently run a function in a higher stack frame
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-Uplevel/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/D/DA/DAGOLDEN/Sub-Uplevel-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(constant)
Requires:       perl(strict)
Requires:       perl(warnings)

%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%prep
%setup -q -n Sub-Uplevel-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING.mkdn cpanfile dist.ini LICENSE META.json perlcritic.rc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.2800-1
- Specfile autogenerated by cpanspec 1.78.
