%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Capture-Tiny
Version:        0.46
Release:        1%{?dist}
Summary:        Capture STDOUT and STDERR from Perl, XS or external programs
License:        Apache Software License
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Capture-Tiny/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(Exporter)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(IO::Handle)
Requires:       perl(Scalar::Util)
Requires:       perl(strict)
Requires:       perl(warnings)

%description
Capture::Tiny provides a simple, portable way to capture almost anything
sent to STDOUT or STDERR, regardless of whether it comes from Perl, from XS
code or from an external program. Optionally, output can be teed so that it
is captured while being passed through to the original filehandles. Yes, it
even works on Windows (usually). Stop guessing which of a dozen capturing
modules to use in any particular situation and just use this one.

%prep
%setup -q -n Capture-Tiny-%{version}

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
%doc Changes CONTRIBUTING.mkdn cpanfile dist.ini LICENSE META.json perlcritic.rc README Todo
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.46-1
- Specfile autogenerated by cpanspec 1.78.
